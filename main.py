import requests
import json
import pandas
import datetime

API = "6de68435eab0e9e311cfc860c6f0ef81"
URL = "https://pro.openweathermap.org/data/2.5/forecast"

parametrs = {
    "lat" : "50.4",
    "lon" : "30.5",
    "cnt" : "7",
    "city" : "Kyiv",
    "country" : "ua",
    "lang" : "ua",
    "units" : "metric",
    "appid" : API
}

response = requests.get(URL,parametrs)
print(response.status_code)

data = response.json()

daily_data =[]
for day in data["list"][:3]:
    daily_data.append({"day" : day["dt_txt"],
        "weather": day["weather"][0]["description"],
        "temp_avg": day["main"]["temp"],
        "temp_min": day["main"]["temp_min"],
        "temp_max": day["main"]["temp_max"],
        "wind_speed" : day["wind"]["speed"]
    })

temp3days = pandas.DataFrame(daily_data)   
avg_wind_speed = temp3days["wind_speed"].mean()
days_above_avg_wind = temp3days[temp3days["wind_speed"] > avg_wind_speed].shape[0]

print("\nWeather Data for 3 Days:")
print(temp3days)
print("\nNumber of days with wind speed above average:", days_above_avg_wind)