import base64
import requests
import json

import os

if 'google_vision_api' in os.environ:
    API_KEY = os.environ['google_vision_api']
else:
    from api_key_module import API_KEY


def encode_image(image):
    image_content = image.read()
    return base64.b64encode(image_content)


def make_post_request(base64_stream):

    # defining the api-endpoint
    API_ENDPOINT = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY


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
