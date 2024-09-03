import requests

api_key = '97864f740b9244528821765942dfbe91'
base_url = 'http://api.weatherbit.io/v2.0/current'
city_name = input("enter you city here:")
url = f"{base_url}?city={city_name}&key={api_key}"
response = requests.get(url)
weather_data = response.json()
print(weather_data)
# print(f"Location: {weather_data['data'][0]['city_name']}")
