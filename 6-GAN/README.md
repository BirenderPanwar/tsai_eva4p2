# GENERATIVE ADVERSARIAL NETWORL

**This is implementation of GAN with R1 Regularizer to generate India Car images. GAM network is build on 700+ car dataset collected through google images.**

# Web Applications

The model is deployed on AWS Lambda using serverless computing framework and the web application is hosted on AWS S3 bucket

**Web Application:** https://s3.ap-south-1.amazonaws.com/www.aijourney.com/eva4p2/s6_gan.html

##

![demo](doc_images/s6_demo_gan.gif)

## Dataset [(link)](https://drive.google.com/file/d/1RT85hbmnCWRHu4Dl9EsJ38urlD1O0KkZ/view?usp=sharing)

700+ Indian car images are collected from google images. For simplicity, car with front facing and specific angle position are collected.

Dataset Size: 704

![sample](doc_images/dataset_samples.jpg)

## GAN Model Creation
 
**Notebook:** S6_R1GAN_Car.ipynb [(Link)](notebooks/S6_R1GAN_Car.ipynb)

```python
batch_size=64
epochs=1000
n_noise = 256 # noise vector size for Generator
```

**Epoch Results**

![result](doc_images/epoch_results.jpg)

**Real and Fake Discriminitive losses**
![result](doc_images/losses_plot.jpg)

**Generative and Discriminitive Losses**
![result](doc_images/d_g_losses_plot.jpg)




