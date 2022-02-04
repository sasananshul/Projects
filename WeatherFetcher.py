import requests

API_KEY = "c088a8623accc2e2af3a7a8b99d2de37"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter your city name: ")

request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    print("Weather: ", weather)
    print("Temperature: ", temperature, " celsius")
else:
    print("An error occurred!")


