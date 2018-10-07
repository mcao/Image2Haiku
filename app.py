import os
import image_data
from flask import Flask, request, render_template, send_from_directory
app = Flask('__name__')


@app.route('/')
def index():
    return render_template("upload.html")


@app.route('/upload', methods=["POST"])
def upload():
    return upload_file(request)


@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files', path)


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

    print(image_data.get_lat_lon(image_data.get_exif_data(destination)))

    return "http://image2haiku.com/files/" + filename


if __name__ == "__main__":
    app.run(port=80, debug=True)
