from urllib.request import urlopen
import json
def getweather():
    api_key ='a0abe46080c5e319d434e512637e8099'
    cityname = input("Enter City Name: ")
    numdays = input("Enter how many days in the future you want data from(1-16): ")
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + str(cityname) + '&cnt=' + str(numdays) +'&appid=' + str(api_key)
    print(url)
    json_obj = urlopen(url)
    data = json.load(json_obj)
    print(str(((int(data['list']['temp']['day'])) - 273.15) * (9 / 5) + 32) + " F")
getweather()

