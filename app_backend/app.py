from flask import Flask, render_template
from app_backend.db_file import search_3days, insert_3days

# RUN SERVER
# curl GET http://localhost:5000/forecast/3_days/London


# sqlalcheny library enables to add pyhton object to tables, take objects from tables..
# it's a tool to work with db in python
from flask_sqlalchemy import SQLAlchemy

import requests

# entity of Flask class
app = Flask(__name__)

# create db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# init db, created instance of SQLAlchemy class, through which we'll work with chosen database (in our case sqlite)
db = SQLAlchemy(app)




# API key is like a login process to web site that Python does
api_key = "cec458e2db4844c9bf693603212811"

# to where goes the request
#url = "http://api.weatherapi.com/v1/current.json?key=cec458e2db4844c9bf693603212811&q=London"

# steps:
# 1. url = ..... (to where we send the request
# 2. response = requests.get(url)
# 3. response_json = response.json()
# 4. pprint.pprint(response_json)    - if we want to print it in a pretty way
# 5. parseForecast(response_json)    - to get relevant fields from json



# forecast for today
#def parseForecastForToday(response_json):
    # location_info = response_json['location']
    # city = location_info['name']
    #
    # for key in location_info:
    #     if key == 'localtime':
    #         date = str(location_info[key]).split(' ')[0]
    #
    # result = response_json['current']
    # for key in result:
    #     if key == 'temp_c':
    #         temp = result[key]
    #
    #     if key == 'feelslike_c':
    #         feels_temp = result[key]
    #
    #     if key == 'humidity':
    #         humidity = result[key]
    #
    #     if key == 'wind_dir':
    #         wind_direction = result[key]
    #
    #
    # # add to db
    # insert_to_db(date, city, str(temp), str(feels_temp), str(humidity), wind_direction)
    #
    # return "Forecast for " + str(date) + " in " + city +":\n" \
    #         "Temperature " + str(temp) + ",\n" \
    #         "Feels like temperature " + str(feels_temp) + ",\n" \
    #         "Humidity " + str(humidity) + ",\n" \
    #         "Wind direction " + str(wind_direction) + "\n"


# forecast for 3 days
# url2 = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=Moscow&days=7"
def parse3DaysForecast(response_json):
    forecast = ""

    res2 = response_json['forecast']['forecastday']
    location = response_json['location']['name']
    values = [location]

    for item in res2:
        for field in item:
            if field == 'astro':
                astro = item[field]
                for key in astro:
                    if key == 'sunrise':
                        sunrise = astro[key]
                        values.append(sunrise)
                    if key == 'sunset':
                        sunset = astro[key]
                        values.append(sunset)


            if field == 'date':
                date = item[field]
                values.append(date)
            if field == 'day':
                info = item[field]
                for key in info:
                    if key == 'avgtemp_c':
                        avg_temp = info[key]
                        values.append(avg_temp)
                    if key == 'mintemp_c':
                        min_temp = info[key]
                        values.append(min_temp)
                    if key == 'maxtemp_c':
                        max_temp = info[key]
                        values.append(max_temp)
                    if key == 'daily_chance_of_rain':
                        rain_possibility = info[key]
                        values.append(rain_possibility)
                    if key == 'daily_chance_of_snow':
                        snow_possibility = info[key]
                        values.append(snow_possibility)
            if field == 'hour':
                info = item[field][0]
                for key in info:
                    if key == 'humidity':
                        humidity = info[key]
                        values.append(humidity)
                    if key == 'pressure_in':
                        pressure = info[key]
                        values.append(pressure)
                    if key == 'wind_dir':
                        wind_direction = info[key]
                        values.append(wind_direction)
                    if key == 'wind_kph':    # kilometer per hour
                        wind_speed = info[key]
                        values.append(wind_speed)


                forecast = forecast + "Forecast for " + str(date) + " in " + location +":\n" \
                       "Minimal temperature " + str(min_temp) + ",\n" \
                       "Maximal temperature " + str(max_temp) + ",\n" \
                       "Average temperature " + str(avg_temp) + ",\n" \
                       "Rain possibility " + str(rain_possibility) + "%,\n" \
                       "Snow possibility " + str(snow_possibility) + "%\n" \
                       "Humidity " + str(humidity) + "\n" \
                       "Pressure " + str(pressure) + "\n" \
                       "Wind direction " + wind_direction + "\n" \
                       "Wind speed " + str(wind_speed) + "\n" \
                       "Sunrise " + str(sunrise) + "\n" \
                       "Sunset " + str(sunset) + "\n\n\n"

    # adding to db
    print("ADD TO DB")
    insert_3days(values)

    return forecast



#@app.route("/forecast/today/<city>", methods=['GET'])
#ef getForecastForToday(city):
    # forecast = search_in_db(city)
    # if forecast is not None:
    #     date = forecast[0]
    #     city = forecast[1]
    #     temperature = forecast[2]
    #     return date + " the temperature in " + city + " is " + temperature + " degrees\n"
    # else:
        #url = "http://api.weatherapi.com/v1/current.json?key=cec458e2db4844c9bf693603212811&q=" + city
    # url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=" + city + "&days=7"
    # response = requests.get(url)
    # if response.status_code is 200:
    #     pprint.pprint(response.json())
    #     return parseForecastForToday(response.json())   # create json from the response, and pass it for parsing
    # return "ERROR"


@app.route("/forecast/3_days/<city>", methods=['GET'])
def getForecastFor3Days(city):
    forecast = search_3days(city)
    if forecast is not None:
        #print("FROM DB")

        return "Weather forecast for 3 next days in " + forecast[0] + "... \n" \
                + "Date: " + forecast[0] + "\n"\
               "Maximal temperature: " + forecast[2] + "\nMinimal temperature: " + forecast[3] + "\nAverage temperature: " + forecast[4] + "\n" \
               "Rain possibility: "  + forecast[5] + "\nSnow possibility: " + forecast[6] + "\n" \
               "Sunrise: " + forecast[7] + "\nSunset: " + forecast[8] + "\n" \
               "Wind speed: " + forecast[9] + "\nWind direction: " + forecast[10] + "\n" \
               "Pressure: " + forecast[11] + "\nHumidity: " + forecast[12] + "\n\n" \
               + "Date: " + forecast[13] + "\n"\
               "Maximal temperature: " + forecast[14] + "\nMinimal temperature: " + forecast[15] + "\nAverage temperature: " + forecast[16] + "\n" \
               "Rain possibility: " + forecast[17] + "\nSnow possibility: " + forecast[18] + "\n" \
               "Sunrise: " + forecast[19] + "\nSunset: " + forecast[20] + "\n" \
               "Wind speed: " + forecast[21] + "\nWind direction: " + forecast[22] + "\n" \
               "Pressure: " + forecast[23] + "\nHumidity: " + forecast[24] + "\n\n" \
               + "Date: " + forecast[25] + "\n"\
               "Maximal temperature: " + forecast[26] + "\nMinimal temperature: " + forecast[27] + "\nAverage temperature: " + forecast[28] + "\n" \
               "Rain possibility: " + forecast[29] + "\nSnow possibility: " + forecast[30] + "\n" \
               "Sunrise: " + forecast[31] + "\nSunset: " + forecast[32] + "\n" \
               "Wind speed: " + forecast[33] + "\nWind direction: " + forecast[34] + "\n" \
               "Pressure: " + forecast[35] + "\nHumidity: " + forecast[36] + "\n"

    else:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=" + city +"&days=7"
        response = requests.get(url)
        if response.status_code == 200:
            return parse3DaysForecast(response.json())
        return "ERROR"




# when we run the application, app = Flask(__name__)   __name__ gets value __main__, so it'll run the local web server
#  http://127.0.0.1:5000/    127.0.0.1 is a local host (local network in our computer),
#  5000 - on this port http server waits for request
if __name__ == '__main__':
    app.run()     # running local web server




@app.route('/about')
def about():
    return render_template('about.html')
