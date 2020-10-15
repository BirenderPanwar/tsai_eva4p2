# NEURAL WORD EMBEDDING - SENTIMENT ANALYSIS FOR INDIAN MOVIE DATASET

**This is implementation of Transformer model for sentiment analysis which analyse the given review commnet as positive or negative sentiment. The model is trained on IMDB dataset using the BERT(Bidirectional Encoder Representations from Transformer) model. Transformers library is used to get pre-trained transformer and use them as embedding layers. We will freeze (not train) the transformer and only train the remainder of the model which learns from the representations produced by the transformer. In this case we will be using a multi-layer bi-directional GRU, however any model can learn from these representations.**

> NOTE
Reference: https://github.com/bentrevett/pytorch-sentiment-analysis
Paper: https://arxiv.org/pdf/1706.03762.pdf (Transformer model)

## Web Application and AWS Lambda Deployment

The model is deployed on AWS Lambda using serverless computing framework and the web application is hosted on AWS S3 bucket

**AWS Deployment Code:** AWS Lambda function and deployment code [(aws-deployment/s9-nwe-aws)](aws-deployment/s9-nwe-aws)
 
**Web Application:** https://s3.ap-south-1.amazonaws.com/www.aijourney.com/eva4p2/s9/nwe/s9_nwer.html

## Web App Demonstration

![demo](doc_images/s9_demo_nwe.gif)


# Transformer Model Creation

**Notebook:** /notebooks/Transformers_for_Sentiment_Analysis.ipynb.ipynb [(Link)](notebooks/Transformers_for_Sentiment_Analysis.ipynb)

**Test Result**
```bash

```

# Another Approach: CNN Model for Sentiment Analysis
In this implementation convolutional neural network (CNN) is used to conduct sentiment analysis

**Notebook:** /notebooks/Convolutional_Sentiment_Analysis [(Link)](notebooks/Convolutional_Sentiment_Analysis.ipynb)

**Test Result**
```bash
Test Loss: 0.357 | Test Acc: 85.35%
```





