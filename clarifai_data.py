from clarifai.rest import ClarifaiApp

API_KEY = "368e6551d02a46b495f9724f7d7d2683"
APP = ClarifaiApp(api_key=API_KEY)


def get_concepts(imgurl, threshold=0.8, max_concepts=100):
    assert isinstance(imgurl, str), "Invalid image input"

    # Set up clarifai api
    model = APP.models.get('general-v1.3')
    prediction = model.predict_by_url(url=imgurl,
                                      max_concepts=max_concepts, min_value=threshold)

    # Get data out of prediction
    return [concept["name"] for concept in prediction["outputs"][0]["data"]["concepts"]]

def get_colors(imgurl, threshold=0.1):
    assert isinstance(imgurl, str), "Invalid image input"

    # List of possible outputs
    outputs = ["white", "grey", "gray", "black", "red",
               "orange", "yellow", "green", "blue", "purple", "violet"]

    # Set up clarifai api
    model = APP.models.get('color')
    prediction = model.predict_by_url(url=imgurl)

    # Get data out of prediction (Get list of data -> Get names if threshold met -> Get list of colors found in outputs -> Remove duplicates)
    color_data = prediction["outputs"][0]["data"]["colors"]
    colors = [color["w3c"]["name"].lower() for color in color_data if color["value"] >= threshold]
    valid_colors = [c for c in outputs for color in colors if c in color]
    return list(set(valid_colors))
