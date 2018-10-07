# image request
import json
import urllib3


def cloud_vision(imageURI='https://cloud.google.com/vision/docs/images/faulkner.jpg'):
    print("Querying cloud vision with URI " + imageURI)
    http = urllib3.PoolManager()
    hardcode = "{'requests':[{'features':[{'type':'FACE_DETECTION','max_results':3},{'type':'LANDMARK_DETECTION','maxResults':3},{'type':'LOGO_DETECTION','maxResults':3},{'type':'LABEL_DETECTION','maxResults':3},{'type':'TEXT_DETECTION','maxResults':3},{'type':'IMAGE_PROPERTIES','maxResults': 3},{'type':'WEB_DETECTION','maxResults':3},{'type':'OBJECT_LOCALIZATION','maxResults':3}],'image':{'source':{'imageUri':'"+imageURI+"'}},'imageContext':{'webDetectionParams':{'includeGeoResults':true}}}]}"
    res = http.request('POST', 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDA0iAWg1ZZsaxdC1xVHxrFeFR6qEMuiKc',
                       body=hardcode, headers={'Content-Type': 'application/json'})
    return res.data


def response(resp):
    vision_response = json.loads(resp.decode('utf-8'))

    # emotions
    try:
        joy = vision_response["responses"][0]["faceAnnotations"][0]["joyLikelihood"]
        sorrow = vision_response["responses"][0]["faceAnnotations"][0]["sorrowLikelihood"]
        anger = vision_response["responses"][0]["faceAnnotations"][0]["angerLikelihood"]
        surprise = vision_response["responses"][0]["faceAnnotations"][0]["surpriseLikelihood"]
        emotions = [joy, sorrow, anger, surprise]
    except:
        emotions = []

    # labels
    labels = []
    for values in range(len(vision_response["responses"][0]["labelAnnotations"])):
        labels.append(vision_response["responses"][0]
                      ["labelAnnotations"][values]["description"])

    # names
    names = []
    if hasattr(vision_response["responses"][0], "localizedObjectAnnotations"):
        print(vision_response["responses"][0]
              ["localizedObjectAnnotations"][0]["name"])
        for values in range(len(vision_response["responses"][0]["localizedObjectAnnotations"])):
            names.append(vision_response["responses"][0]
                         ["localizedObjectAnnotations"][0]["name"])
    elif hasattr(vision_response["responses"][0], "webEntities"):
        print(vision_response["responses"][0]["webEntities"][0]["description"])
        for values in range(len(vision_response["responses"][0]["webEntities"])):
            names.append(vision_response["responses"]
                         [0]["webEntities"][0]["description"])

    # concanate objects
    objects = names + labels

    return emotions, objects


def black_magic(emotions):
    if emotions == []:
        return 0, False, False

    happiness = 0
    anger = False
    surprise = False

    if emotions[0] == "VERY_LIKELY":
        happiness += 1
    elif emotions[0] == "LIKELY":
        happiness += 0.5
    if emotions[1] == "VERY_LIKELY":
        happiness -= 1
    elif emotions[1] == "LIKELY":
        happiness -= 0.5
    if emotions[2] == "VERY_LIKELY" or emotions[2] == "LIKELY":
        anger = True
    if emotions[3] == "VERY_LIKELY" or emotions[3] == "LIKELY":
        surprise = True

    return (happiness, anger, surprise)


if __name__ == "__main__":
    print(response(cloud_vision()))
