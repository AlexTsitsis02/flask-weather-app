from flask import Flask, render_template, request
import sqlite3
import requests

app = Flask(__name__)

# Function to fetch live weather data from OpenWeatherMap API
def get_live_weather(city_name):
    api_key = 'a8b53c92aeb9ddace6352d85d0e75c5b'  # Replace with your API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return (
            data['name'],
            f"{data['main']['temp']}°C",
            data['weather'][0]['description'],
            f"{data['wind']['speed']} m/s",
            f"{data['main']['humidity']}%"
        )

    except requests.exceptions.RequestException as e:
        print(f"Weather API Error: {e}")
        return None

# Function to fetch cities from the local database
def fetch_local_cities():
    try:
        connection = sqlite3.connect('weather_data.db')
        cursor = connection.cursor()
        cursor.execute("SELECT city FROM weather")
        cities = cursor.fetchall()
        connection.close()
        return [city[0] for city in cities]
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return []

# Predefined list of cities for online fetching (from OpenWeatherMap)
def fetch_online_cities():
    return [
        "Berlin", "Los Angeles", "Moscow", "Cairo", "Rio de Janeiro",
        "Cape Town", "Seoul", "New York", "Paris", "Tokyo",
        "Toronto", "Sydney", "London", "Mexico City", "Mumbai",
        "Beijing", "Rome", "Barcelona", "Chicago", "Buenos Aires",
        "Amsterdam", "Athens", "Dubai", "Stockholm", "Warsaw", "Istanbul"
    ]

# Main route for weather data
@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    weather_data = None

    local_cities = fetch_local_cities()
    online_cities = [city for city in fetch_online_cities() if city not in local_cities]

    if request.method == 'POST':
        city_name = request.form.get('city_name', '').strip()
        if city_name:
            weather_data = get_live_weather(city_name)

            if weather_data:
                message = f"Weather data for {weather_data[0]} fetched successfully!"
            else:
                message = f"Error: Unable to fetch weather data for {city_name}."
        else:
            message = "Please enter a valid city name."

    return render_template('index.html', message=message, weather_data=weather_data,
                           local_cities=local_cities, online_cities=online_cities)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

