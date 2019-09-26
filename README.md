## Smart-recipe

## State of the Problem
Help people improve their cooking by allowing them to simply follow along a recipe, and not have to deal with distractions like touchscreen or voice commands. 
![](https://user-images.githubusercontent.com/20251285/65660347-50579c80-dfe3-11e9-8eee-c71c47cd32a8.jpg)

## Hardware

Our design includes: 
Fully wireless, compact and comfortable watch style enclosure for our Raspberry pi 0 w, accelerometer, and a Powerboost 500C. Includes a rechargeable battery, and a switch to the control power. 

![](https://user-images.githubusercontent.com/20251285/65660538-d8d63d00-dfe3-11e9-90ad-8381874d5715.jpg)
![](https://user-images.githubusercontent.com/20251285/65660542-daa00080-dfe3-11e9-868c-95d0fb3e2319.jpg)

## Software

Front end: Website interface that interacts with the user and displays new steps to the recipe as you complete different motions in your cooking. Automatically changes recipe steps while cooking based on detecting the motion.

Backend: Data collection and processing done on Raspberry Pi on the wrist watch, then fed to the Firebase database. We store our model on Azure, which is an LSTM model that can be repeatedly trained and can predict whenever the frontend wants a prediction.  

![](https://user-images.githubusercontent.com/20251285/65660631-281c6d80-dfe4-11e9-87e3-1db90f771011.png)
![](https://user-images.githubusercontent.com/20251285/65660680-44b8a580-dfe4-11e9-814e-9a26e63640dd.png)

## Website

![](https://user-images.githubusercontent.com/20251285/65660783-a2e58880-dfe4-11e9-8041-7982c05f81af.png)
![](https://user-images.githubusercontent.com/20251285/65660785-a416b580-dfe4-11e9-9e1d-043b27b95038.png)
