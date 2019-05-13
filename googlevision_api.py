import base64
import requests
import json
from api_key_module import API_KEY
from flask import jsonify

def encode_image(image):
    image_content = image.read()
    return base64.b64encode(image_content)


def make_post_request(base64_stream):

    # importing the requests library


    # defining the api-endpoint
    API_ENDPOINT = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY

    # retrieved form creating project and asking for credentials
    

    # your source code here


    # data to be sent to api
    base64_stream_string = base64_stream.decode('utf-8')
    json_request = {
        "requests": [
            {
                "image": {
                    "content": base64_stream_string
                },
                "features": [
                    {
                        "type": "TEXT_DETECTION"
                    }
                ]
            }
        ]
    }

    # sending post request and saving response as response object
    response = requests.post(url=API_ENDPOINT, data=json.dumps(json_request))
    return response
