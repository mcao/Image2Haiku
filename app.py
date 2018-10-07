import os
import image_data
import clarifai_data
import haiku_generator
import weather
import image_request
from flask import Flask, request, render_template, send_from_directory
app = Flask('__name__')


@app.route('/')
def index():
    return render_template("upload.html")


@app.route('/upload', methods=["POST"])
def upload():
    file_data = upload_file(request)
    ext = os.path.splitext(upload.filename)[1]
    if ext is 'jpg':
        lat, lon = image_data.get_lat_lon(
            image_data.get_exif_data(file_data[0]))
    else:
        lat, lon = None
    url = file_data[1]

    try:
        concepts = clarifai_data.get_concepts(url)
        colors = clarifai_data.get_colors(url)
    except:
        return "Kill Yourself"

    emotions, objects = image_request.response(image_request.cloud_vision(url))
    emotion_data = image_request.black_magic(emotions)

    phrases = removeDuplicates(concepts, objects)

    if lat is not None and lon is not None:
        weather_raw = weather.get_weather(weather.get_city(lat, lon))
        weather_data = weather.black_magic(weather_raw, emotion_data[0])
    else:
        weather_data = weather.black_magic({"WeatherIcon": -1,
                                            "Temp": "20.0C",
                                            "IsDaylight": True}, emotion_data[0])
    print(phrases, colors, emotion_data, weather_data)
    return haiku_generator.generate_haiku(phrases, colors, emotion_data, weather_data)


@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files', path)


def removeDuplicates(list1, list2):
    outlist = []
    inlist = list1 + list2
    for item in inlist:
        item = item.lower()
        if item not in outlist:
            outlist.append(item)
    return outlist


def upload_file(req):
    target = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in req.files.getlist("file"):
        filename = file.filename
        destination = target + "/" + filename
        print("Accepted incoming file: ", filename)
        print("File saved: ", destination)
        file.save(destination)

    return (destination, "http://image2haiku.com/files/" + filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
