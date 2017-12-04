# Emerging-Technologies-Project
### Assignment for Emerging Technologies Module - 4th Year Software Development
### Ríona Greally - G00325504

This Assignment is a Webpage that when you upload a hand-written or likewise image, a prediction of what figurethe image is of is displayed.

[Flask](https://www.fullstackpython.com/flask.html) is a microframework for python and is used for example for mapping to different pages of a web page.

[Tensorflow](https://www.tensorflow.org/) is a Neural Network. I used Tensorflow to create and train the model I use for predictiong the digit images. 

[Numpy](http://www.numpy.org/) is the fundamental package for scientific computing with Python. Numpy takes care of all the mathemetical functions for python. 

[MNIST](http://yann.lecun.com/exdb/mnist/) dataset contains handwritten image files. It consists of a training set of 60,000 images and a test set which has 10,000 images. 

## Running the Application
#### 1. Git Clone this Repo
#### 2. Using CMDER, direct into the folder repository
#### 3. Run the python file by running the command:
    
     py app.py
   
#### 4. Go to the url given in cmder: 

     http://127.0.0.1:5000/
     
#### 5. Upload a image of a handwritten digit or like the ones in the images folder


## Project Instructions

The following are your instructions to complete the project for the module Emerging Technologies for 2017. This project is worth 40% of your marks for the module. Please see the course homepage for the deadline.

### Overview

In this project you will create a web application in Python to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image. You should use tensorflow and flask to do this. Note that accuracy of approximately 99% is considered excellent in recognising digits, so it is okay if your algorithm gets it wrong sometimes.

### Instructions

1. Create a git repository with a README.md and an appropriate gitignore file. The README should explain who you are, why you created the application, how you created it, how to download and run it, and summarise any references you have used.
2. In the repository, create a web application that serves a HTML page as the root resource. The page should contain an input where the user can upload (or draw) an image containing a digit, and an area to display the image and the digit.
3. Add a route to your application that accepts requests containing a user input image and responds with the digit.
4. Connect the HTML page to the route using AJAX.

[Link to Intructions](https://emerging-technologies.github.io/problems/project.html)
