import requests
import os
import dataModel

OPENWEATHER_APIKEY = os.getenv("openweather_apikey")
MAPBOX_APIKEY = os.getenv("mapbox_apikey")


def get_location(city_name: str, temp_system: str) -> dataModel.CityModel:
    link = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{city_name}.json?access_token={MAPBOX_APIKEY}"
    res = requests.get(link)
    if res.status_code == 200:
        feats = res.json()["features"]
        if len(feats) < 1:
            print("City not found")
            exit()
        city_desc = feats[0]["place_name"]
        lon = feats[0]["center"][0]
        lat = feats[0]["center"][1]
        return dataModel.CityModel(city_name=city_name, city_desc=city_desc, lat=lat, lon=lon, temp_system=temp_system)
    else:
        print(f"Error\nSomething went wrong. StatusCode: {res.status_code}")
        exit()


def get_weather(city_model: dataModel.CityModel) -> dataModel.WeatherModel:
    link = f"https://api.openweathermap.org/data/2.5/onecall?lat={city_model.lat}&lon={city_model.lon}&appid={OPENWEATHER_APIKEY}&units={city_model.temp_system}&exclude=minutely,alerts,daily"
    res = requests.get(link)
    if res.status_code == 200:
        current_temp = res.json()["current"]["temp"]
        current_cond = res.json()["current"]["weather"][0]["description"]
        future_cond = res.json()["hourly"][4]["weather"][0]["description"]
        return dataModel.WeatherModel(
            city_details=city_model.city_desc,
            temp_unit="C" if city_model.temp_system == "metric" else "F",
            condition=current_cond,
            temp=current_temp,
            future_condition=future_cond
        )
    else:
        print(f"Error\nSomething went wrong. StatusCode: {res.status_code}")
        exit()
