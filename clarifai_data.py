from clarifai.rest import ClarifaiApp

API_KEY = "368e6551d02a46b495f9724f7d7d2683"
APP = ClarifaiApp(api_key=API_KEY)


def get_concepts(imgurl='https://samples.clarifai.com/metro-north.jpg', threshold=0.8, max_concepts=100):
    model = APP.models.get('general-v1.3')
    prediction = model.predict_by_url(url=imgurl,
                                      max_concepts=max_concepts, min_value=threshold)

    # Get data out of prediction
    concepts = prediction["outputs"][0]["data"]["concepts"]
    valid_concepts = []
    for concept in concepts:
        if concept["value"] >= threshold:
            valid_concepts.append(concept["name"])

    return valid_concepts


def get_colors(imgurl='https://samples.clarifai.com/metro-north.jpg', threshold=0.1):
    model = APP.models.get('color')
    prediction = model.predict_by_url(url=imgurl)

    # Get data out of prediction
    colors = prediction["outputs"][0]["data"]["colors"]
    valid_colors = []
    for color in colors:
        if color["value"] >= threshold:
            color_name = color["w3c"]["name"].lower()
            color_names = ["white", "grey", "gray", "black", "red",
                           "orange", "yellow", "green", "blue", "purple", "violet"]
            for c in color_names:
                if c in color_name and c not in valid_colors:
                    valid_colors.append(c)
    return valid_colors
