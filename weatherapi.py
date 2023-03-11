import requests

url = 'http://api.weatherapi.com/v1/current.json?key='
key = "0ea9cb1d78ac4314add10211231003"
location = "&q=Hayward"
params = {
    "key":"0ea9cb1d78ac4314add10211231003",
    "q":94542,
}
data = {"positions":[0,6,7,29]}

#url = "http://api.weatherapi.com/v1/current.json?key=0ea9cb1d78ac4314add10211231003&q=Hayward&aqi=no"
url = url + key + location
r = requests.post(url)

print(r.status_code)
print(r.json())