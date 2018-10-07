import os
import requests

from flask import Flask, request, render_template, send_from_directory

app = Flask('__name__')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template("upload.html")
    # this is the function for calling the render template


@app.route('/upload', methods=["POST"])
# method for uploading the file
def upload():
    return uploadFile(request)


@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files', path)


def uploadFile(request):
    # this is to verify that folder to upload to exists.
    # if os.path.isdir(os.path.join(APP_ROOT, 'files')):
    #     print("folder exist")

    target = os.path.join(APP_ROOT, 'files')
    # print(target)
    # print the file name
    # print("-------------------------------------------")
    if (not os.path.isdir(target)):
        os.mkdir(target)
    '''
    print("good target")
    print("-------------------------------------------")
    # if the directory exists, good. if not, then make it
    print(request.files.getlist("files"))
    # print the list of files requested...i think
    '''

    for upload in request.files.getlist("file"):
        # print(upload)
        # print('{} is the file name'.format(upload.filename))
        filename = upload.filename
        # this is to verify that files are supported
        '''
        ext = os.path.splitext(filename)[1]
        if (ext == ".jpg") or (ext == ".png"):
            print("File is supported...moving on")
        else:
            render_template(
                "error.html", message="Files were not supported: "+ext)
        print("-------------------------------------------")
        '''
        # adds the target directory path to the string filename with the / seperator
        destination = target + "/" + filename
        print("Accepted incoming file: ", filename)
        print("File saved: ", destination)
        # print("-------------------------------------------")
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    # will show the file icon and tell that it is completed
    return "http://image2haiku.com/files/" + filename


if __name__ == "__main__":
    app.run(port=80, debug=True)
