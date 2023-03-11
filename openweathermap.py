# import required modules
import requests, json
from datetime import datetime

# Enter your API key here
api_key = "81a92e33853cee3579c39858c4a07aa1"

# base_url 
base_url = "http://api.openweathermap.org/data/2.5/weather?" #for 1 day
base_url = "http://api.openweathermap.org/data/2.5/forecast?zip=94542,us" #for 5 day forcast
# api.openweathermap.org/data/2.5/forecast?zip=94040,us&appid={API key}
# api.openweathermap.org/data/2.5/forecast?lat={37.6688}&lon={122.0810}&appid={API key}

# Give city name
# city_name = input("Enter city name : ")
city_name = "hayward"

# complete_url variable to store
# complete url address
# complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric" #for 1 day weather
complete_url = base_url + "&appid=" + api_key + "&units=metric" #for forcast

# get method of requests module
# return response object
response = requests.get(complete_url)
x = response.json()

#for 1 day
# print(datetime.fromtimestamp(x['dt']).strftime('%d-%m-%y'))
# print(x['weather'])


#for forcast
print(x['list'])
# if x["cod"] != "404":
 
#     # store the value of "main"
#     # key in variable y
#     y = x["main"]
 
#     # store the value corresponding
#     # to the "temp" key of y
#     current_temperature = y["temp"]
 
#     # store the value corresponding
#     # to the "pressure" key of y
#     current_pressure = y["pressure"]
 
#     # store the value corresponding
#     # to the "humidity" key of y
#     current_humidity = y["humidity"]
 
#     # store the value of "weather"
#     # key in variable z
#     z = x["weather"]
 
#     # store the value corresponding
#     # to the "description" key at
#     # the 0th index of z
#     weather_description = z[0]["description"]
 
#     # print following values
#     print(" Temperature (in kelvin unit) = " +
#                     str(current_temperature) +
#           "\n atmospheric pressure (in hPa unit) = " +
#                     str(current_pressure) +
#           "\n humidity (in percentage) = " +
#                     str(current_humidity) +
#           "\n description = " +
#                     str(weather_description))
 
# else:
#     print(" City Not Found ")