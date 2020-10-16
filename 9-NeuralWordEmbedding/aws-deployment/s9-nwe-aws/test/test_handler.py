#from handler import main_handler
from handler import main_handler
import json
import io
from models.transformers_net import BERTGRUSentiment

textData = "This film is great"

def test_handler():
    body = json.dumps({"text": textData})
    resp = main_handler({
        'headers': {'content-type': 'application/json'},
        'body': body
    }, '')
    resp_body = json.loads(resp['body'])
    print(resp['statusCode'])
    print(resp_body)
    assert resp['statusCode'] == 200

if __name__ == '__main__':
    print("Running test..")
    test_handler()