#image request
import json
import urllib3

def cloud_vision(imageURI = 'https://cloud.google.com/vision/docs/images/faulkner.jpg'):
	http = urllib3.PoolManager()
	hardcode = "{'requests':[{'features':[{'type':'FACE_DETECTION','max_results':3},{'type':'LANDMARK_DETECTION','maxResults':3},{'type':'LOGO_DETECTION','maxResults':3},{'type':'LABEL_DETECTION','maxResults':3},{'type':'TEXT_DETECTION','maxResults':3},{'type':'IMAGE_PROPERTIES','maxResults': 3},{'type':'WEB_DETECTION','maxResults':3},{'type':'OBJECT_LOCALIZATION','maxResults':3}],'image':{'source':{'imageUri':'"+imageURI+"'}},'imageContext':{'webDetectionParams':{'includeGeoResults':true}}}]}"
	response = http.request('POST', 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDA0iAWg1ZZsaxdC1xVHxrFeFR6qEMuiKc', body = hardcode , headers = {'Content-Type':'application/json'})
	return response.data

def response(response):
	vision_response = json.loads(response)

	#emotions
	try:
		joy      = vision_response["responses"][0]["faceAnnotations"][0]["joyLikelihood"]
		sorrow   = vision_response["responses"][0]["faceAnnotations"][0]["sorrowLikelihood"]
		anger    = vision_response["responses"][0]["faceAnnotations"][0]["angerLikelihood"]
		surprise = vision_response["responses"][0]["faceAnnotations"][0]["surpriseLikelihood"]
		emotions = [joy, sorrow, anger, surprise]
	except:
		emotions = []

	#labels
	labels = []
	for values in range(len(vision_response["responses"][0]["labelAnnotations"])):
		labels.append(vision_response["responses"][0]["labelAnnotations"][values]["description"])

	#names
	names = []
	print(vision_response["responses"][0]["localizedObjectAnnotations"][0]["name"])
	for values in range(len(vision_response["responses"][0]["localizedObjectAnnotations"])):
		names.append(vision_response["responses"][0]["localizedObjectAnnotations"][0]["name"])

	#concanate objects
	objects = names + labels

	return emotions, objects

if __name__ == "__main__":
	print(response(cloud_vision ()))

