import requests

city = input("Enter a city: ")

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]
city_name = geo_data["results"][0]["name"]

forecast = "https://api.open-meteo.com/v1/forecast"
forecast_params = {"latitude": lat, "longitude": lon, "current": ["temperature_2m", "rain"], "temperature_unit": "fahrenheit"}

forecast_response = requests.get(forecast, params=forecast_params)
forecast_data = forecast_response.json()

temp = forecast_data["current"]["temperature_2m"]
rain = forecast_data["current"]["rain"]

print (f"In {city_name}🏢: ")
print (f"The temperature is🌡️: {temp}F")
print (f"The rain is💦: {rain}mm")
