import requests

def get_weather_forecast():
    #Get weather data from openweathermap.org
    url = "http://api.openweathermap.org/data/2.5/weather?q=roseville,us&&units=imperial&appid=401f319ee0e7297f674604d0f649fe09"
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    print(weather_json)

    description = weather_json['weather'][0]['description']
    print(description)

    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = 'The weather forecast for today is ' + description + ' with a high of ' + str(temp_max) + ' and a low of ' + str(temp_min)
    return forecast
