#/usr/bin/python3
import io
def detect_text( path ):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')
    #print(texts)
    textList=[]
    for text in texts:
        textList.append(text.description)
    return textList
photo = "index.png"
copyList = detect_text(photo)
copyList=copyList[1:]
print(copyList)

