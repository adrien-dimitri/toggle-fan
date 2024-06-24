import os
import requests, json

def get_temperature(lat, lon, api_key):
   
    api_call = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    response = requests.get(api_call)
    print(response)
    data = response.json()

    if data['cod'] != '404':
        main = data['main']

        curr_temp = main['feels_like']

        curr_temp_celsius = (curr_temp - 273.15)

        return round(int(curr_temp_celsius), 2)

    else:
        return None

