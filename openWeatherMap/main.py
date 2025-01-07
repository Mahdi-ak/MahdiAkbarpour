
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  
        "lang": "fa"        
    }
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            print("JSON response:\n" ,response.json())
            data = response.json()
            print("\nWeather information for", city)
            print(f"city: {data['name']}")
            print(f"temp: {data['main']['temp']}°C")
            print(f"Status: {data['weather'][0]['description']}")
            print(f"Wind speed: {data['wind']['speed']} Meters per second")
        else:
            print("error:", response.json().get("message", "request error"))
    except Exception as e:
        print("error:", e)



city = input("Enter city name: ")
api_key = "85e19a58499c974bfb08396f2bcd2410"  # Replace with your OpenWeatherMap API key
get_weather(city, api_key)