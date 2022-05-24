# Vegetable_Classification
![my badge](https://img.shields.io/badge/Python-3-blue)
![my badge](https://img.shields.io/badge/Deep-Learning-brightgreen)
![my badge](https://img.shields.io/badge/Flask-App-green)
![my badge](https://img.shields.io/badge/Image-Classification-yellowgreen)
![my badge](https://img.shields.io/badge/Tensorflow-2-orange)
![my badge](https://img.shields.io/badge/-Docker-purple)
![my badge](https://img.shields.io/badge/-GIT-green)

# About The Project

This project has been developed to classify vegetable images.

# Project Description 

A web app has been developed for this project which takes a image as an input and returns the predictions as a result. The app is dockerized and pushed to dockerhub. Command to pull the image from dockerhub is given below. The object detection model is trained using Tensorflow 2 using Google Colab. The input image is first encode to base64 format after which is it send to the backend where the image is decoded and the prediction is done. And final ly the input image 

# Dataset Used

This dataset is taken from Kaggle and more information about the dataset can be found below.

Dataset : [Link](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset)

# Project Structure


<img width="223" alt="image" src="https://user-images.githubusercontent.com/58848985/169962590-ab070ba9-6002-4c02-8665-cadd9d9b7de0.png">


* com_in_ineuron_ai_utils - This directory contains the script for all necessary function
* templates - This directory contains the frontend files for the webapp
* TL_TF_VGG.h5 - This file contains the trained weights of the VGG model

# Preview of the WebApp

Web App Main page :

<img width="960" alt="image" src="https://user-images.githubusercontent.com/58848985/161686467-240d553e-17c3-471b-974d-9a5e786e0edb.png">

Web after Prediction : 

<img width="960" alt="image" src="https://user-images.githubusercontent.com/58848985/161686649-ecd0019d-6b09-4464-8cf8-e838facf270b.png">

Docker command to pull the image:

```docker pull techner3/vegclassifier```
