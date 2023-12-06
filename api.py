import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, request
import numpy as np

model = load_model('./static/letter-recognizer.h5')


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/letter", methods=["POST"])
def get_letter():
    data = request.data.decode()
    print(data)
    array = np.array([[[float(value)] for value in row.split(", ")] for row in data.split("\n")])
    predicted_value = predict(array)
    return predicted_value


labels = [
   "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T" , "U", "V", "W", "X", "Y", "Z"
]

def predict(array):
   array = np.array([array])
   prediction = model.predict(array)
   index = np.argmax(prediction, axis=1)[0]
   return labels[index]