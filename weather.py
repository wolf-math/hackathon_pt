# remember to install deps
import os
import requests
import json
from dotenv import load_dotenv

# secrets are stored in .env file.
load_dotenv()

# gets the specific secret called "WEATHER_API"
api_key = os.getenv('WEATHER_API')

# lat and long of DI
lat, long = (32.08717459733143, 34.80154524594145)

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}"

response = requests.get(url)

res_json = response.json()

print(res_json)