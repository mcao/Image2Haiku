from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='368e6551d02a46b495f9724f7d7d2683')
CONFIDENCE_THRESHOLD = 0.8

model = app.models.get('general-v1.3')
prediction = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
print("finished prediction")

# Get data out of prediction
concepts = prediction["outputs"][0]["data"]["concepts"]
valid_concepts = []
for concept in concepts:
    if concept["value"] >= CONFIDENCE_THRESHOLD:
        valid_concepts.append(concept["name"])
        
print(valid_concepts)