# Transport-not-transport App
This machine learning powered app that tells you whether an image contains a mode of transport or not. <br>
http://transport-not-transport-app.herokuapp.com/

<img src="https://user-images.githubusercontent.com/73251461/151224043-c80dd60a-51f2-43d2-87eb-09106687330e.png" width="900">

# Dataset
The model was trained on 25000 images of transport and not transport downloaded from ImageNet. 

Here's a brief summary of the data collection process:
1. Created a list containing 580 types of transport along with their respective synids (unique ID to identify each ImageNet class).
2. Created a list containing the synids of 500 randomly selected non-transport classes. 
3. Used `downloader.py` from `ImageNet-Datasets-Downloader` (link [here](https://github.com/mf1024/ImageNet-Datasets-Downloader)) to download 30 images of each class from ImageNet
4. Merged folders of each class containing their respective images into a larger sub-directory of transport and not-transport images. 

# Model Building

# Deployment
