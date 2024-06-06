import os
import time
from flask import Flask, jsonify, request, render_template, send_from_directory, url_for
from functions.crop import imgcrop, imgcropurl
from config import config
import requests
from os import remove
import random
from PIL import Image
import io

app = Flask(__name__)


@app.after_request
def after_request(response):
    # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/split-url', methods=['POST'])
def create_user():
    data = request.get_json()
 
    data_url = (data['url'])
    data_row = (data['row'])
    data_col = (data['col'])
    return imgcropurl(data_url,data_row, data_col)


@app.route('/split-images-example', methods=['GET'])
def default():
    data = request.get_json()
    data_row = data['row']
    data_col = data['col']

    images_array = ['1.jpeg', '2.jpeg', '3.jpeg', '4.jpeg', '5.jpeg']
    image_selected = images_array[random.randint(0, 4)]
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
    image_url = url_for('static', filename=f'images/{image_selected}')  # Construir la URL de la imagen

    return jsonify({"image_url": image_url})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(host="0.0.0.0", port=5000, debug=True)
