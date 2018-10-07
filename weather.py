import requests
API_KEY = "HackPSU2018"
BASE_URL = "http://dataservice.accuweather.com/"


def get_weather(location):
    location_url = BASE_URL + "locations/v1/search?q=" + \
        location.replace(' ', '%20') + "&apikey=" + API_KEY
    req = requests.get(url=location_url)
    data = req.json()

    temp = "done"

    weather_url = BASE_URL + "forecasts/v1/hourly/1hour/" + \
        data[0]["Key"] + "?apikey=" + API_KEY

    req = requests.get(url=weather_url)
    data = req.json()

    temp = str(data[0]["Temperature"]["Value"]) + \
        data[0]["Temperature"]["Unit"]
    res = {"IconPhrase": data[0]["IconPhrase"],
           "Temp": temp,
           "IsDaylight": data[0]["IsDaylight"]}

    return res


def get_city(latitude, longitude):
    # get the city using longitude and latitude here
    
    loc_url = BASE_URL + "locations/v1/cities/geoposition/search?apikey=" + API_KEY + "&q="
    loc_url = loc_url + str(latitude) + "%2C" + str(longitude)
    
    print(loc_url)
    
    req = requests.get(url=loc_url);
    
    data = req.json()
    
    if data is None:
        return "FUCK YOURSELF"
    else:
        return data["LocalizedName"]
