from ctypes import resize
from PIL import Image
from os import remove
import base64
import time
from io import BytesIO
import traceback
import requests
import io

def imgcropurl(url, xPieces, yPieces):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(url)
        response.raise_for_status()  # Esto lanzará una excepción si la descarga falla
        im_ = Image.open(io.BytesIO(response.content))
        
        # Redimensionar la imagen a 500x500
        resize_ = (500, 500)
        im = im_.resize(resize_)
        
        imgwidth, imgheight = im.size
        height = imgheight // yPieces
        width = imgwidth // xPieces
        
        array = []
        for i in range(yPieces):
            for j in range(xPieces):
                box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
                a = im.crop(box)
                b64im = image_to_base64(a)
                string_b64_img = b64im.decode('UTF-8')
                array.append({"url": "data:image/jpeg;base64," + string_b64_img, "id": [i, j]})
                
        return array
    except Exception as e:
        tb_str = traceback.format_exc()
        return {
            'error': f"Error type: {type(e).__name__}",
            'message': f"Error message: {str(e)}",
            "Traceback details": tb_str
        }
    

def imgcrop(input, xPieces, yPieces):
    try:
        array = []
        im_ = Image.open(input)
        resize_ = (500, 500)
        im = im_.resize(resize_)
        imgwidth, imgheight = im.size
        height = imgheight // yPieces
        width = imgwidth // xPieces
        for i in range(0, yPieces):
            for j in range(0, xPieces):
                box = (j * width, i * height, (j + 1)
                       * width, (i + 1) * height)
                a = im.crop(box)
                a.save("img.jpg")
                b64im = image_to_base64("img.jpg")
                string_b64_img = b64im.decode('UTF-8')
                # print(type(string_b64_img))
                array.append({"url": "data:image/jpg;base64," +
                              string_b64_img, "id": [i, j]})
                time.sleep(.2)
                remove("img.jpg")
        return array
    except Exception as e:
        tb_str = traceback.format_exc()
        return {
            'error': f"Error type: {type(e).__name__}",
            'message': f"Error message: {str(e)}",
            "Traceback details": tb_str
        }


def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue())
