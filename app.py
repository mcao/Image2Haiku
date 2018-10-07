import os
import image_data
import clarifai_data
import haiku_generator
import weather
from flask import Flask, request, render_template, send_from_directory
app = Flask('__name__')


@app.route('/')
def index():
    return render_template("upload.html")


@app.route('/upload', methods=["POST"])
def upload():
    file_data = upload_file(request)

    lat, lon = image_data.get_lat_lon(image_data.get_exif_data(file_data[0]))
    url = file_data[1]

    concepts = clarifai_data.get_concepts(url)
    colors = clarifai_data.get_colors(url)

    city = weather.get_city(lat, lon)
    weather_data = weather.get_weather(city)

    return haiku_generator.generate_haiku(concepts, colors, weather_data)


@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files', path)

def removeDuplicates(clarifaiList, visionList):
    outlist = clarifaiList[:]
    for item in visionList:
        if item not in clarifaiList:
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
    app.run(port=80, debug=True)
