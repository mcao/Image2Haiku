from flask import Flask, request, render_template
import json
import requests

__author__ = 'mrmitty'

app=Flask(__name__)

APIKEY = "HackPSU2018"

@app.route('/',methods=['GET'])
def index():
    #print("ready")
    locationURL = "http://dataservice.accuweather.com/locations/v1/search?q=State%20College&apikey=HackPSU2018"
    r = requests.get(url=locationURL)
    #print(r);
    data = r.json()
    #print("--------------------------------------")

#key = request.json[locationURL,'Key']
#    print(key)
#print(data[0]["Key"])
    
    # for x in data:
    #   try:
    #       print(x, data[x]["Key"])
    #   except:
    #       print("error")

#print("done")
    temp = "done"
    
    weatherURL = "http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/" + data[0]["Key"] + "?apikey=" + APIKEY
    
    r = requests.get(url=weatherURL)
    
    print(r.content)
    
    data = r.json()
    
    #print(data[0]["IconPhrase"])
    #print(data[0]["Temperature"]["Unit"],data[0]["Temperature"]["Value"])

    temp = str(data[0]["Temperature"]["Value"]) + data[0]["Temperature"]["Unit"]
    res = {"IconPhrase":data[0]["IconPhrase"],
            "Temp":temp,
        "IsDaylight":data[0]["IsDaylight"]}
    #thomas code
    #print(type(r))
    #print(r.content)
    
    return res
    


def iterate(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            iterate(value)
            continue
    print('key {!r} -> value {!r}'.format(key, value))
