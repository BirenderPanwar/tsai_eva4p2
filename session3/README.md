## Session-3: 
* **Face Alignment**
* **Face Swaping**
* **Using Serverless framework, Lambda function for the model is deployed onto AWS**
* **Web page application is hosted on AWS S3 bucket**

## Package Structure

<p align="center"><img style="max-width:800px" src="doc_images/folder_structure.png"></p>

## Face Alignment

* Face Alignment using 5-Points Landmark detector by DLIB
* In the new 5-point model, the landmark points consist of 2 points at the corners of the eye; for each eye and one point on the nose-tip
* To perform Face Alignment, first detect 5 Points landmarks and compute the normalized image by using the similarity transform

Notebook: S3_FaceAlignment_5PointModel.ipynb [(Link)](notebooks/S3_FaceAlignment_5PointModel.ipynb)

AWS Deployment: [(Link)](aws_deployment/s3-face-align-aws)


## Face Swap

* Select any two person image with front face.
* It finds 68 points landmarks for both the faces using DLIB
* It finds Convex Hull from second image and calculate mask for seamless cloning
* It find Delaunay traingulation for convex hull points for both the images
* Finally, it apply affine transformation to Delaunay triangles and perform clone seamlessly

Notebook: S3_FaceSwap.ipynb [(Link)](notebooks/S3_FaceSwap.ipynb)

AWS Deployment: [(Link)](aws_deployment/s3-face-swap-aws)

### API Request Message
```
# img1_base64 and img1_base64: this contains image data in base64 encoded format

{
	"img1": img1_base64,
	"img2": img2_base64
}
```

### API Response Message
```
# Function to convert numpy image data into base64 encoded format for web ui
def img_to_base64(img):
    img = Image.fromarray(img, 'RGB') 
    buffer = io.BytesIO()
    img.save(buffer,format="JPEG")
    myimage = buffer.getvalue()                     
    img_str = f"data:image/jpeg;base64,{base64.b64encode(myimage).decode()}"
    return img_str

# swapped image data is convered into base64 encoded format for rendering on HTML
swapped_face = get_face_swap(image_bytes1=im1, image_bytes2=im2)
im_base64 = img_to_base64(swapped_face)

# Response Message Body
{
	"swappedFacImg": im_base64,
	"img2": img2_b64
}
```

## Testing Stategy

File: test_handler.py [(Link)](aws_deployment/s3-face-align-aws/test/test_handler.py)

```
# im1_base64data : base64 encoded data of test image1 
# im2_base64data : base64 encoded data of test image2 

def test_handler(im1_str, im2_str):
    body = json.dumps({"img1": im1_str, "img2": im2_str})
    resp = main_handler({
        'headers': {'content-type': 'application/json'},
        'body': body
    }, '')
    resp_body = json.loads(resp['body'])
    print(resp['statusCode'])
    #print(resp_body)
    #assert resp_body['something'] == 208


if __name__ == '__main__':
    print("Running test..")
    test_handler(im1_base64data, im2_base64data)
```

## Web App for Image Classification (RESNET Model) [(Visit)](https://s3.ap-south-1.amazonaws.com/www.aijourney.com/s1_demo.html)
## Web App for Drone Classification using MobileNet_V2 pre-trained model [(Visit)](https://s3.ap-south-1.amazonaws.com/www.aijourney.com/s2_demo.html)
## Web App for Face Alignment [(Visit)](https://s3.ap-south-1.amazonaws.com/www.aijourney.com/s3_face_align.html)
## Web App for Face Swap [(Visit)](https://s3.ap-south-1.amazonaws.com/www.aijourney.com/s3_face_swap.html)


**Face Align Web Link:** https://s3.ap-south-1.amazonaws.com/www.aijourney.com/s3_face_align.html

<p align="center"><img img style="max-width:400px" src="doc_images/face_align_app.png"></p>


**Face Swap Web Link:** https://s3.ap-south-1.amazonaws.com/www.aijourney.com/s3_face_swap.html

<p align="center"><img img style="max-width:400px" src="doc_images/face_swap_app.png"></p>




