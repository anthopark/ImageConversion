import base64


def encode_image(image):
    image_content = image.read()
    return base64.b64encode(image_content)


def make_post_request(base64_stream):

    # importing the requests library
    import requests

    # defining the api-endpoint
    API_ENDPOINT = "https://vision.googleapis.com/v1/images:annotate"

    # your API key here
    # retrieved form creating project and asking for credentials
    API_KEY = ''

    # your source code here
    source_code = '''
    print("Hello, world!")
    a = 1
    b = 2
    print(a + b)
    '''
    # no source code needed i think?

    # data to be sent to api
    json_request = {
        "requests": [
            {
                "image": {
                    "content": base64_stream
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION",
                        "maxResults": 1
                    }
                ]
            }
        ]
    }

    # sending post request and saving response as response object
    response = requests.post(url=API_ENDPOINT, data=json.dumps(request))

    return response
