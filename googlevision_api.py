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
    API_KEY = "AIzaSyAFVBJtv1oR6ZmJhX6-BBdnmJxvxSt7Heo" #retrieved form creating project and asking for credentials

    # your source code here
    source_code = '''
    print("Hello, world!")
    a = 1
    b = 2
    print(a + b)
    '''
    # no source code needed i think?

    # data to be sent to api
    json_request =  {
  "requests":[
    {
      "image":{
        "content":"/9j/7QBEUGhvdG9...image contents...eYxxxzj/Coa6Bax//Z"
      },
      "features":[
        {
          "type":"LABEL_DETECTION",
          "maxResults":1
        }
      ]
    }
  ]
}
    


    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = json.dumps(request))

    # extracting response text
    json_response = r.text


    
