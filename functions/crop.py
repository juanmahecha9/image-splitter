from ctypes import resize
from PIL import Image
from os import remove
import base64
import time
from io import BytesIO
import traceback


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


def image_to_base64(image_path):
    img = Image.open(image_path)
    output_buffer = BytesIO()
    img.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str
