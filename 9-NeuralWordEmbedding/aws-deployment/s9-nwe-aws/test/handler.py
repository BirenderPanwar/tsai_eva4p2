try:
    import unzip_requirements
except ImportError:
    pass

import torch
import transformers
from transformers import BertTokenizer

import boto3
import os
import io
import json
from models.transformers_net import BERTGRUSentiment

print("Import End...")

# define env variables if there are not existing
S3_BUCKET = os.environ['S3_BUCKET'] if 'S3_BUCKET' in os.environ else 'biru-eva4p2'
MODEL_PATH = os.environ['MODEL_PATH'] if 'MODEL_PATH' in os.environ else 'session9/nwe_transformer_model_cpu.pt'

print('Downloading model: ' + MODEL_PATH)

# load the S3 client when lambda execution context is created
s3 = boto3.client('s3')

def load_model_from_s3():
    try:
        if os.path.isfile(MODEL_PATH) != True:
            obj = s3.get_object(Bucket=S3_BUCKET, Key=MODEL_PATH)
            print('Creating bytestream')
            bytestream = io.BytesIO(obj['Body'].read())
            print('Loading model')
            model = torch.load(bytestream)
            print('Model loaded')
            return model
        else:
            print('Model loading failed')
    except Exception as e:
        print(repr(e))
        raise(e)

t_model = load_model_from_s3()

print('Downloading tokenizer')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
print('Downloaded tokenizer')

init_token_idx = tokenizer.cls_token_id
eos_token_idx = tokenizer.sep_token_id
pad_token_idx = tokenizer.pad_token_id
unk_token_idx = tokenizer.unk_token_id

max_input_length = tokenizer.max_model_input_sizes['bert-base-uncased']
print(max_input_length)

def predict_sentiment(model, tokenizer, sentence):
    model.eval()
    tokens = tokenizer.tokenize(sentence)
    tokens = tokens[:max_input_length-2]
    indexed = [init_token_idx] + tokenizer.convert_tokens_to_ids(tokens) + [eos_token_idx]
    tensor = torch.LongTensor(indexed)
    tensor = tensor.unsqueeze(0)
    prediction = torch.sigmoid(model(tensor))
    return prediction.item()


def main_handler(event, context):
    try:
        content_type_header = event['headers']['content-type']
        print('content_type header: ' + content_type_header)
        #print('Event Body: ' + event["body"])

        json_body = json.loads(event["body"])
        
        textMsg = json_body["text"]
        print(f'text: {textMsg}')

        pred = predict_sentiment(t_model, tokenizer, textMsg)      
        print(f'Prediction: {pred}')

        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            "body": json.dumps({'prediction': pred})
        }
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True
            },
            "body": json.dumps({"error": repr(e)})
        }
