from flask import Flask, render_template,  request, redirect, url_for, send_from_directory
from PIL import Image  

import numpy as np
import flask as fl
import json
import os, base64, io, re

# adapted from https://www.tensorflow.org/get_started/mnist/beginners

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf


#creating variables that tensorflow uses and represents as a 2-D tensor of floating-point numbers(NONE: meaning a dimension of any lenght)
x = tf.placeholder(tf.float32, [None, 784])

#[784, 10] : this multiplies the 784 dimensional image by vectors by w to produce a 10 dimensional vetors
W = tf.Variable(tf.zeros([784, 10]))
# b's shape of 10 is added to the output
b = tf.Variable(tf.zeros([10]))

#Defining our model
# x is multiplied by W and then b is added onto the result and then applying softmax regression
y = tf.nn.softmax(tf.matmul(x, W) + b)

#Training the model
# adding variable y for the correct answers to be stored
y_ = tf.placeholder(tf.float32, [None, 10])

#implementing the cross-entropy function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

#training the model with minimal cross_entropy and using gradient decent of 0.5
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#launching model
sess = tf.InteractiveSession()

#initillizing variables
tf.global_variables_initializer().run()

# training the model 1000 times
# getting batches of 100 random data sets from our training set and feeding them into s
for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

#Accuracy
# retrieving a lidt of booleans to find what % that's correct 
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

# getting the accuracy of the test and printing it out
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

app = fl.Flask(__name__)


#routing to the index.html
@app.route("/")
def route():
	return app.send_static_file("index.html")
	


@app.route("/model", methods=['GET','POST'])
def upload():
	if request.method == 'POST':
		print('in post')
		image = request.values["image"]
		imgstr = re.search(r'base64,(.*)', image).group(1)
		print(image)
		data = image.rsplit(',', 1)[1]
		image_bytes = io.BytesIO(base64.b64decode(imgstr))
		im = Image.open(image_bytes)
		# Image.ANTIALIAS minimises distortion when representing a high-resolution image at a lower resolution
		im = im.resize((28, 28), Image.ANTIALIAS)
		def normalize(x):
			return x / 256

		normalize = np.vectorize(normalize, otypes=[np.float32])
		ary = normalize(np.array(im, dtype=np.float32)[:,:,0])
		ary = ary.flatten().tolist()
		classification = sess.run(tf.argmax(y, 1), feed_dict={x: [ary]})
		print('NN predicted', classification[0])
		return str(classification[0])
	return "Opps something went wrong"


if __name__ == "__main__":
	app.run()