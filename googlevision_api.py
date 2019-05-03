import base64

def encode_image(image):
    image_content = image.read()
    return base64.b64encode(image_content)


def make_post_request(base64_stream):


    
