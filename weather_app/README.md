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

<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Django</title><path d="M11.146 0h3.924v18.166c-2.013.382-3.491.535-5.096.535-4.791 0-7.288-2.166-7.288-6.32 0-4.002 2.65-6.6 6.753-6.6.637 0 1.121.05 1.707.203zm0 9.143a3.894 3.894 0 00-1.325-.204c-1.988 0-3.134 1.223-3.134 3.365 0 2.09 1.096 3.236 3.109 3.236.433 0 .79-.025 1.35-.102V9.142zM21.314 6.06v9.098c0 3.134-.229 4.638-.917 5.937-.637 1.249-1.478 2.039-3.211 2.905l-3.644-1.733c1.733-.815 2.574-1.53 3.109-2.625.561-1.121.739-2.421.739-5.835V6.059h3.924zM17.39.021h3.924v4.026H17.39z"/></svg>