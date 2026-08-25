from fastapi import FastAPI,HTTPException
import os
from dotenv import load_dotenv
import requests

app = FastAPI()

load_dotenv()

API_KEY = os.getenv("API_KEY")

@app.get("/get_lon_and_lat")
def get_lon_lat(city_name:str,state_code:str,country_code:str,limit:int=2):
    URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}"
    response = requests.get(URL)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="lat log  not found for this location"
        )
    
    return response.json()

@app.get("/current_weather_data")
def current_weather_data(lat:str,lon:str):
    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(URL)
    if response.status_code != 200:
           raise HTTPException(
               status_code=404,
               detail="weather not found for this location"
           )
       
    return response.json()