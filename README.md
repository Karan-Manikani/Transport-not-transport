# Transport-not-transport App
This machine learning powered app tells you whether an image contains a mode of transport or not. <br>
http://transport-not-transport-app.herokuapp.com/

<img src="https://user-images.githubusercontent.com/73251461/151224043-c80dd60a-51f2-43d2-87eb-09106687330e.png" width="900">

## Dataset
The model was trained on a dataset containing 25000 images downloaded from ImageNet. The dataset included 14000 images of different types of transport and 11000 images of the not transport class.
Here's a summary of the data collection process:
1. Created a list containing 580 types of transport along with their respective synids (unique ID to identify each ImageNet class). 
2. Created a list containing the synids of 500 randomly selected non-transport classes. 
3. Used `downloader.py` from `ImageNet-Datasets-Downloader` (link [here](https://github.com/mf1024/ImageNet-Datasets-Downloader)) to download 30 images per class from ImageNet. 
4. Merged folders of each class to form a larger sub-directory of transport and not-transport images. 

## Model Building
Built and trained a CNN using transfer learning in Tensorflow. Two dense layers were stacked on top of a fine-tuned EfficientNet base model which outputs a value between 0 and 1. Data augmentation was applied to all images before being sent into the CNN for training. 

Model metrics:
* Training Accuracy: 95.19 %
* Validation Accuracy: 93.96 %
* Testing Accuracy: 94.76 %

## Deployment
The front-end UI of the web app was made using Streamlit. It includes a file uploader widget that allows you to upload images, and a predict button that returns predictions along with the probability of the predicted class.<br>
The web app was deployed to Heroku. <br>
You can find the web app [here](http://transport-not-transport-app.herokuapp.com/)
