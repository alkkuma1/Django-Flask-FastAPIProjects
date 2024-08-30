if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition, showError);
} else {
    alert("Geolocation is not supported by this browser.");
}

const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
const monthsOfYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

function showPosition(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    fetch(`/get_weather?lat=${lat}&lon=${lon}`)
        .then(response => response.json())
        .then(data => {
            displayWeatherData(data.weather_data, data.forecast_data);
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
        });
}
function showError(error) {
    alert("Unable to retrieve your location due to " + error.message);
}
function displayWeatherData(weather_data, forecast_data) {
    const weatherContainer = document.createElement('div');
    weatherContainer.className = 'city-container';

    weatherContainer.innerHTML = `
        <h2>Current Location: ${weather_data.city}, ${ weather_data.country }</h2>
        <h3>Temperature: ${weather_data.temprature}°C</h3>
        <p>You should experience ${weather_data.description}.
        <img src="http://openweathermap.org/img/w/${weather_data.icon}.png" alt="${weather_data.description}">
        </p>
        <h2>5 Day Forecast:</h2>
    `;

    const forecastContainer = document.createElement('div');
    forecastContainer.className = 'forecast-container';
    const table = document.createElement('table');

    const tableHead = document.createElement('thead');
    const tableHeadings = ['Day', 'Temperature', 'Description'];
    const tableBody = document.createElement('tbody');
    tableRow = document.createElement('tr');
    tableHeadings.forEach(heading => {
        const th = document.createElement('th');
        th.textContent = heading;
        tableRow.appendChild(th);
    });

    tableHead.appendChild(tableRow);
    table.appendChild(tableHead);
    forecastContainer.appendChild(table);
    
    forecast_data.forEach(forecast => {
        tableRow = document.createElement('tr');
        tableRow.innerHTML = `
            <td>${forecast.date}</td>
            <td>${forecast.temprature}°C</td>
            <td>${forecast.description} <img src="http://openweathermap.org/img/w/${forecast.icon}.png" alt="${forecast.description}"></td>
        `;
        tableBody.appendChild(tableRow);
        table.appendChild(tableBody);
    });

    weatherContainer.appendChild(forecastContainer);
    document.body.appendChild(weatherContainer);
}
