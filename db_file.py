import sqlite3
import datetime

#> PYTHON DB_FILE.PY (RUN FILE)


conn = sqlite3.connect("weather.db", check_same_thread=False)
                            # it will connect to db, and if db with passed name doesn't exist
                           # it'll be created, and than we'll connect to it

# create cursor (using this object we'll be able to perform different things with db)
cursor = conn.cursor()

# create table
# there are only 5 data types that SQLite work with: NULL, INTEGER (whole number), REAL (float), TEXT,
# BLOB (something which is stored exactly as it is, for example image)
# cursor.execute("""CREATE TABLE weather_forecast(
#     date text,
#     location text,
#     temperature text,
#     feels_like text,
#     humidity text,
#     wind_direction text
#     )""")
#
# cursor.execute("""CREATE TABLE weather_forecast_3days(
#         location text,
#         day1_date text,
#         max_temp_day1 text,
#         min_temp_day1 text,
#         avg_temp_day1 text,
#         rain_pos_day1 text,
#         snow_pos_day1 text,
#         sunrise_day1 text,
#         sunset_day1 text,
#         wind_speed_day1 text,
#         wind_dir_day1 text,
#         pressure_day1 text,
#         humidity_day1 text,
#
#         day2_date text,
#         max_temp_day2 text,
#         min_temp_day2 text,
#         avg_temp_day2 text,
#         rain_pos_day2 text,
#         snow_pos_day2 text,
#         sunrise_day2 text,
#         sunset_day2 text,
#         wind_speed_day2 text,
#         wind_dir_day2 text,
#         pressure_day2 text,
#         humidity_day2 text,
#
#         day3_date text,
#         max_temp_day3 text,
#         min_temp_day3 text,
#         avg_temp_day3 text,
#         rain_pos_day3 text,
#         snow_pos_day3 text,
#         sunrise_day3 text,
#         sunset_day3 text,
#         wind_speed_day3 text,
#         wind_dir_day3 text,
#         pressure_day3 text,
#         humidity_day3 text
#     )""")

#cursor.execute("DROP TABLE weather_forecast_3days")

# cursor.execute("INSERT INTO weather_forecast VALUES ('2021-12-01', 'Jerusalem', '12', '11', '82', 'N')")
# cursor.execute("INSERT INTO weather_forecast VALUES ('2021-12-01', 'Moscow', '2', '-1', '90', 'N')")
#
# #insert many elements
# forecast_3days = [
#                     ('1/12/2021', 'London', '3', '1', '30', 'SW'),
#                     ('2/12/2021', 'London', '2', '0', '50', 'W'),
#                     ('3/12/2021', 'London', '-1', '-3', '85', 'N')
#                 ]
# cursor.executemany("INSERT INTO weather_forecast VALUES(?,?,?,?,?,?)", forecast_3days)
#


# values = list of values that we add to db
def insert_3days(values):
    cursor.executemany("INSERT INTO weather_forecast_3days VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [values])
    conn.commit()

    #check that things where added
    #print("ADDED")
    #cursor.execute("SELECT * FROM weather_forecast_3days")
    #print(cursor.fetchall())


def search_3days(city):
    cursor.execute("SELECT * FROM weather_forecast_3days WHERE location = ? ", [city])
    data = cursor.fetchone()
    print(data)
    if data is None:
        return data
    else:
        if data[1] == str(datetime.date.today()):
            return data

        # in case that we have record with wanted city, but date isn't relevant
        cursor.execute("DELETE from weather_forecast_3days WHERE location = ?", [city])
        conn.commit()  # think that need
        return None

# SQLite parameter substitution problem !!!
def insert_to_db(date, city, temperature, feels_like, humidity, wind_direction):
    data_to_insert = [(date, city, temperature, feels_like, humidity, wind_direction)]
    cursor.executemany("INSERT INTO weather_forecast VALUES(?,?,?,?,?,?)", data_to_insert)
    #cursor.execute("INSERT INTO weather_forecast VALUES (? ? ? ? ? ?) ", [date, city, temperature, feels_like, humidity, wind_direction])
    conn.commit()

    print("added")
    cursor.execute("SELECT * FROM weather_forecast")
    print(cursor.fetchall())


# this function should get city parameter that will be passed to the query
def search_in_db(city):
    cursor.execute("SELECT * FROM weather_forecast WHERE location = ? ", [city])
    data = cursor.fetchone()
    print(data)
    if data is None:
        return data
    else:
        if data[0] == str(datetime.date.today()):
            return data

        # in case that we have record with wanted city, but date isn't relevant
        cursor.execute("DELETE from weather_forecast WHERE location = ?", [city])
        conn.commit()    # think that need
        return None

#cursor.execute("DELETE from weather_forecast WHERE location = 'Moscow'")
cursor.execute("SELECT * FROM weather_forecast_3days")

#print(cursor.fetchall())
table_rows = cursor.fetchall()
for row in table_rows:
    print(row)


# It will commit the transaction that means all the changes saved to the database.
conn.commit()

# close connection
#conn.close()