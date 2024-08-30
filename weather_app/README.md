# A simple Weather Comparator
<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="40" height="40"><title>Django</title><path d="M11.146 0h3.924v18.166c-2.013.382-3.491.535-5.096.535-4.791 0-7.288-2.166-7.288-6.32 0-4.002 2.65-6.6 6.753-6.6.637 0 1.121.05 1.707.203zm0 9.143a3.894 3.894 0 00-1.325-.204c-1.988 0-3.134 1.223-3.134 3.365 0 2.09 1.096 3.236 3.109 3.236.433 0 .79-.025 1.35-.102V9.142zM21.314 6.06v9.098c0 3.134-.229 4.638-.917 5.937-.637 1.249-1.478 2.039-3.211 2.905l-3.644-1.733c1.733-.815 2.574-1.53 3.109-2.625.561-1.121.739-2.421.739-5.835V6.059h3.924zM17.39.021h3.924v4.026H17.39z"/></svg><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>JavaScript</title><path d="M0 0h24v24H0V0zm22.034 18.276c-.175-1.095-.888-2.015-3.003-2.873-.736-.345-1.554-.585-1.797-1.14-.091-.33-.105-.51-.046-.705.15-.646.915-.84 1.515-.66.39.12.75.42.976.9 1.034-.676 1.034-.676 1.755-1.125-.27-.42-.404-.601-.586-.78-.63-.705-1.469-1.065-2.834-1.034l-.705.089c-.676.165-1.32.525-1.71 1.005-1.14 1.291-.811 3.541.569 4.471 1.365 1.02 3.361 1.244 3.616 2.205.24 1.17-.87 1.545-1.966 1.41-.811-.18-1.26-.586-1.755-1.336l-1.83 1.051c.21.48.45.689.81 1.109 1.74 1.756 6.09 1.666 6.871-1.004.029-.09.24-.705.074-1.65l.046.067zm-8.983-7.245h-2.248c0 1.938-.009 3.864-.009 5.805 0 1.232.063 2.363-.138 2.711-.33.689-1.18.601-1.566.48-.396-.196-.597-.466-.83-.855-.063-.105-.11-.196-.127-.196l-1.825 1.125c.305.63.75 1.172 1.324 1.517.855.51 2.004.675 3.207.405.783-.226 1.458-.691 1.811-1.411.51-.93.402-2.07.397-3.346.012-2.054 0-4.109 0-6.179l.004-.056z"/></svg>

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