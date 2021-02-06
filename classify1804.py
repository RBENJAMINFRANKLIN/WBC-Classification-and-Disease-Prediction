# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image C:/Users/HP/PycharmProjects/BloodFlask/Algorithm-Backpropogation/examples/Basophile.1.bmp

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
from flask import Flask, app,render_template


app = Flask(__name__)

def classify(filenameforclassify,wbccount,wbcvariation):
 filepath=filenameforclassify
 print("file path at classify is = "+filepath)
 im = cv2.imread(filepath)
 output = im.copy()

# pre-process the image for classification
 image = cv2.resize(im, (96, 96))
 print("image resizes in classify")
 image = image.astype("float") / 255.0
 image = img_to_array(image)
 image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network and the label
# binarizer
 print("[INFO] loading network...")
 model = load_model("model")
 lb = pickle.loads(open("labelbin", "rb").read())

# classify the input image
 print("[INFO] classifying image...")
 proba = model.predict(image)[0]
 idx = np.argmax(proba)
 label = lb.classes_[idx]

 NotBloodCell=label
 print(label)

#build the label and draw the label on the image
 label = "{}: {:.2f}%".format(label, proba[idx] * 100)
 output = imutils.resize(output, width=400)
 cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)

#show the output image
 print("[INFO] {}".format(label))
 cv2.imshow("Output", output)
 cv2.waitKey(0)


#classify("C:/Users/Nayan/PycharmProjects/Blood1505/TestData/car3.jpg")