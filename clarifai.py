from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import colorsys

app = ClarifaiApp(api_key='368e6551d02a46b495f9724f7d7d2683')


def getConcepts(imgurl='https://samples.clarifai.com/metro-north.jpg', CONFIDENCE_THRESHOLD=0.8, MAX_CONCEPTS=100):
    model = app.models.get('general-v1.3')
    prediction = model.predict_by_url(url=imgurl, max_concepts=MAX_CONCEPTS, min_value=CONFIDENCE_THRESHOLD)

    # Get data out of prediction
    concepts = prediction["outputs"][0]["data"]["concepts"]
    valid_concepts = []
    for concept in concepts:
        if concept["value"] >= CONFIDENCE_THRESHOLD:
            valid_concepts.append(concept["name"])

    return valid_concepts

def getColors(imgurl='https://samples.clarifai.com/metro-north.jpg', PERCENT_THRESHOLD=0.1, MAX_CONCEPTS=100):
    model = app.models.get('color')
    prediction = model.predict_by_url(url=imgurl)

    # Get data out of prediction
    colors = prediction["outputs"][0]["data"]["colors"]
    valid_colors = []
    for color in colors:
        # if color["value"] >= PERCENT_THRESHOLD:
        #     r = int(color["w3c"]["hex"][1:3], 16)/255
        #     g = int(color["w3c"]["hex"][3:5], 16)/255
        #     b = int(color["w3c"]["hex"][5:], 16)/255
        #     hsv = colorsys.rgb_to_hsv(r,g,b)
        #     print(hsv)
        if color["value"] >= PERCENT_THRESHOLD:
            colorName = color["w3c"]["name"].lower()
            colorNames = ["white","grey","gray","black","red","orange","yellow","green","blue","purple","violet"]
            for c in colorNames:
                if c in colorName and c not in valid_colors:
                    valid_colors.append(c)
    return valid_colors