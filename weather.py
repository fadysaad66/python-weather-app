"""A Flask web application that displays weather information."""
from flask import Flask
import requests

app = Flask(__name__)


class Weather:
    """Handles weather data fetching and presentation."""

    def __init__(self, name, lat, lon, units = "metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            respond = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?units={self.units}"
                    f"&lat={self.lat}&lon={self.lon}"
                    f"&appid=94887d3b472a40e81dd35185dfe5616e",
                    timeout=20
            )

            respond_json = respond.json()
            self.temp = respond_json["main"]["temp"]
            self.max_temp = respond_json["main"][ "temp_max"]
            self.min_temp = respond_json["main"][ "temp_min"]
        except:
            print("error check your internet")
        

    def print_tem(self):
        unit_sample = "c"
        if self.units == "imperial":
          unit_sample = "F"
        #print(f"the temp in {self.name}  is {self.temp} {unit_sample}")
        #print(f"the max temp in {self.name} is {self.max_temp} {unit_sample}")
        #print(f"the min temp in {self.name} is {self.min_temp} {unit_sample}")
        return(f"<p>the temp in {self.name} is {self.temp} {unit_sample}</p>"
               f"<p>the max temp in {self.name} is {self.max_temp} {unit_sample}</p>"
               f"<p>the min temp in {self.name} is {self.min_temp} {unit_sample}</p>")

@app.route("/")
def home():
    city1 = Weather("Dubai", 25.276987, 55.296249,)
    city2 = Weather("los Angeles",34.098907, -118.327759, units = "imperial" )
    output = city1.print_tem() + city2.print_tem()
    return f"<h1>Weather Report</h1>{output}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) 
