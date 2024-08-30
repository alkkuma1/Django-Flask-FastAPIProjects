import datetime 
from django.http import JsonResponse
import requests
from django.shortcuts import render
import json


API_KEY = open('API_KEY', "r").read()
current_weather_url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}&units=metric"

# Create your views here.
def index(request):
    if request.method == "POST":
        city1 = request.POST.get('city1')
        city2 = request.POST.get('city2', None)
        if city1:
            lat, long = get_coords_from_city(city1, API_KEY)
            weather_data1, forecast_data1 = fetch_weather_data(lat, long, current_weather_url, forecast_url, API_KEY)
        else:
            weather_data1, forecast_data1 = None, None
        if city2:
            lat, long = get_coords_from_city(city2, API_KEY)
            weather_data2, forecast_data2 = fetch_weather_data(lat, long, current_weather_url, forecast_url, API_KEY)
        else:
            weather_data2, forecast_data2 = None, None
        context = {
            "weather_data1": weather_data1,
            "forecast_data1": forecast_data1,
            "weather_data2": weather_data2,
            "forecast_data2": forecast_data2
        }
        return render(request, "weather_app/index.html", context)
    else:
        return render(request, "weather_app/index.html")
    
def get_coords_from_city(city, API_KEY):
    url = "http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}"
    response = requests.get(url.format(city, API_KEY)).json()
    lat = response[0]["lat"]
    long = response[0]["lon"]
    return lat, long

def get_weather(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    weather_data, forecast_data = fetch_weather_data(lat, lon, current_weather_url, forecast_url, API_KEY)
    response_data = {
        'weather_data': weather_data,
        'forecast_data': forecast_data
    }
    return JsonResponse(response_data)

def fetch_weather_data(lat, long, current_weather_url, forecast_url, API_KEY):
    current_response = requests.get(current_weather_url.format(lat, long, API_KEY)).json()
    weather_data = {
        "city": current_response['name'],
        "country": current_response['sys']['country'],
        "temprature": current_response['main']['temp'],
        "description": current_response['weather'][0]['description'],
        "icon": current_response['weather'][0]['icon']
    }
    
    forecast_response = requests.get(forecast_url.format(lat, long, API_KEY)).json()
    daily_forecast = []
    for daily_forecast_item in forecast_response['list'][7::8]:
        human_readable_date = datetime.datetime.fromtimestamp(daily_forecast_item['dt']).strftime("%A,  %B %d")
        daily_forecast.append(
            {
                "date": human_readable_date,
                "temprature": daily_forecast_item['main']['temp'],
                "description": daily_forecast_item['weather'][0]['description'],
                "icon": daily_forecast_item['weather'][0]['icon']
            }
        )
    return weather_data, daily_forecast
    
    