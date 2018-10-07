import os
import requests
from flask import Flask, request, render_template, send_from_directory
app = Flask('__name__')


@app.route('/')
def index():
    return render_template("upload.html")


@app.route('/upload', methods=["POST"])
def upload():
    return uploadFile(request)


@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files', path)


def uploadFile(request):
    target = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')
    if (not os.path.isdir(target)):
        os.mkdir(target)

    for upload in request.files.getlist("file"):
        filename = upload.filename
        destination = target + "/" + filename
        print("Accepted incoming file: ", filename)
        print("File saved: ", destination)
        upload.save(destination)

    return "http://image2haiku.com/files/" + filename


if __name__ == "__main__":
    app.run(port=80, debug=True)
