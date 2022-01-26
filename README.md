# Transport-not-transport App
This machine learning powered app that tells you whether an image contains a mode of transport or not. <br>
http://transport-not-transport-app.herokuapp.com/

<p float="left">
<img src="https://user-images.githubusercontent.com/73251461/151202142-8fdd47fd-e84f-4c6b-9954-c6d0d227d7a4.png" width="600">
<img src="https://user-images.githubusercontent.com/73251461/151201732-b5eeffdc-e64a-4f7f-a9d1-0afe444ff37c.png" width="600">
</p>

# Dataset
The model was trained on 25000 images of transport and not transport downloaded from ImageNet. 

Here's a brief summary of the data collection process:
1. Created a list containing 580 types of transport along with their respective synids (unique ID to identify each ImageNet class).
2. Created a list containing the synids of 500 randomly selected non-transport classes. 
3. Used `downloader.py` from `ImageNet-Datasets-Downloader` (link [here](https://github.com/mf1024/ImageNet-Datasets-Downloader)) to download 30 images of each class from ImageNet
4. Merged folders of each class containing their respective images into a larger sub-directory of transport and not-transport images. 

# Model Building

# Deployment
