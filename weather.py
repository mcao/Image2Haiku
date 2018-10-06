import flask from Flask request

app=Flask(__name__)

@app.route('/')
def index():
    locationURL = "https://dataservice.accuweather.com/locations/v1/searc?q=State College&apikey=HackPSU2018"
    r = requests.get(url = locationURL)
    print(r)
    
