API_KEY = 'your_api_key_here'
import requests

def get_weather(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    return {'temperature': temperature, 'description': description, 'humidity': humidity, 'wind_speed': wind_speed}
    location = 'Harare'
weather = get_weather(location)
print(f'The temperature in {location} is {weather["temperature"]} Kelvin, with {weather["description"]}. The humidity is {weather["humidity"]}% and the wind speed is {weather["wind_speed"]} meters/second.')
