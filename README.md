# Django-Flask-FastAPIProjects

## This repository contains the projects I am doing for Django, FastAPI and Flask.

1. weather_app - A simple weather app to display weather to 2 cities alongwith the weather of your current location.
# A simple Weather Comparator

A web application that compares weather data for two different locations, including a 5-day forecast. The application uses Django for the backend and JavaScript for fetching and displaying weather data on the frontend.

<details>
  <summary>Table of Contents</summary>
  <ul>
  		<li> <a href="#Features">Features</a> </li>
        <li><a href="#Installation">Installation</a></li>
      	<li><a href="#Usage">Usage</a></li>
      	<li><a href="#Project Structure">Project Structure</a></li>
      	<li><a href="#API Integration">API Integration</a></li>
  </ul>
</details>
![image](https://github.com/user-attachments/assets/943d1981-c9f3-4aad-9aa5-c6a9bba5f1d0)

## Features

- Fetch and display current weather data for two different locations.
- Display a 5-day weather forecast for each location.
- Responsive UI that places the weather information side by side for easy comparison.
- Integration with OpenWeatherMap API.

## Installation
### Prerequisites
- Python 3.x
- Django 4.x
- A valid API key from <a href="https://openweathermap.org/"> OpenWeatherMap </a>

### Setup
#### 1. Get a free API key from <a href="https://openweathermap.org/"> OpenWeatherMap </a>
#### 2. Clone the repository
```sh
https://github.com/alkkuma1/Django-Flask-FastAPIProjects/tree/main/weather_app
```
#### 3. Install required dependencies from requirements.txt
#### 4. Add API_KEY
Create a filename "API_KEY" and paste the generated API key. File should have single line. File should be in the root directory.
#### 5. Run the Django development server.
```sh
python manage.py runserver
```
#### 6. Access the application
Open your browser and navigate to http://127.0.0.1:8000/.

## Usage
### Comparing Weather Data
-  Enter the names of two cities in the provided text fields.
- Click the "Compare weather" button.
- The current weather and 5-day forecast for both cities will be displayed side by side.

## Project Structure
```
weather_app/
│
├── weather_app/               # Django project directory
│   ├── static/                # Static files (CSS, JS, images)
│   │   ├── index.js           # JavaScript file for fetching weather data
│   │   └── styles.css         # Custom CSS styles
│   ├── templates/weather_app             # HTML templates
│   │   ├── city_weather.html          # Partial template for city weather
│   │   ├── index.html         # Main page template
│   ├── settings.py             # Settings python file
│   ├── urls.py             # Overall URL routing
├── weatherapp/               # Django application directory
│   ├── apps.py                # Configure and manage the app
│   ├── urls.py                # App specific URL routing
│   ├── urls.py                # Main Django code
```

## API Integrations
Weather data is fetched using the OpenWeatherMap API.
### Fetching GeoLocation
The JavaScript code retrieves the user's location via the Geolocation API and sends a request to the Django backend.
"http://api.openweathermap.org/geo/1.0/direct?q={}&limit=1&appid={}"
### Fetching weather data
Django backend fetches the weather data and passes the required elements to HTML using below API.
"https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric"
### Fetching weather forecast data
Django backend fetches the weather data and passes the required elements to HTML using below API.
"https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}&units=metric"
