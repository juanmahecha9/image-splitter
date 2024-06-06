import os
import time
from flask import Flask, jsonify, request, render_template
from functions.crop import imgcrop
from config import config
import requests
from os import remove
import random

app = Flask(__name__)


@app.after_request
def after_request(response):
    # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/slicer/image', methods=['POST'])
def create_user():
    data = request.get_json()
    # Descarga de la imagen temporalmente
    if (os.path.exists('url_file.jpg')):
        remove("url_file.jpg")
    if (os.path.exists('img.jpg')):
        remove("img.jpg")
    time.sleep(0.001)
    with open('url_file.jpg', 'wb') as file:
        file.write(requests.get(data["url"]).content)
    time.sleep(0.01)
    images = imgcrop("./url_file.jpg", int(data["row"]), int(data["col"]))
    time.sleep(.01)
    remove("url_file.jpg")
    return jsonify(images)


@app.route('/api/split-images', methods=['GET'])
def default():
    images_array = ['1.jpeg', '2.jpeg', '3.jpeg', '4.jpeg', '5.jpeg']
    data = request.get_json()
    path = os.path.dirname(os.path.abspath(__file__))
    images = imgcrop(
        path + "/images/"+images_array[random.randint(0, 4)], int(f'{data[0]}'), int(f'{data[1]}'))
    return images


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(host="0.0.0.0", port=5000, debug=True)
