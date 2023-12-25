import os
import requests
import json
city= input("Enter the name of city you want to know temperature")
url= f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r=requests.get(url)
print(r.text)
dictionary=json.loads(r.text)
s=(dictionary["current"]["temp_c"])
h=(dictionary["current"]["humidity"])
d=(dictionary["current"]["wind_kph"])
os.system(f"say 'the current temperature in {city} is {s} degree celcius. Humidity is {h}.and the wind is blowing with a speed of{d}kilometer per hour'")