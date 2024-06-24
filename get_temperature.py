from dotenv import load_dotenv
import os
import requests, json

load_dotenv()

lat = os.getenv('LAT')
lon = os.getenv('LON')
api_key = os.getenv('API_KEY')

api_call = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

response = requests.get(api_call)

data = response.json()

if data['cod'] != '404':
    main = data['main']

    curr_temp = main['feels_like']

    curr_temp_celsius = (curr_temp - 273.15)

    print(curr_temp_celsius)

else:
    print("Not found")

