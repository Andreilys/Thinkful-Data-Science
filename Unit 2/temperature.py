import time
import datetime
import requests
import sqlite3 as lite
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
#This is for the SQLite table to create unique_id to identify the data storage
unique_ID = 100000



#get data from weather API, return a list of JSON data from all the 5 cities
def getData(API_key, cities, date):
    atlanta = requests.get("https://api.forecast.io/forecast/" + API_key + "/" + cities["Atlanta"] + "," + date).json()
    austin = requests.get("https://api.forecast.io/forecast/" + API_key + "/" + cities["Austin"] + "," + date).json()
    boston = requests.get("https://api.forecast.io/forecast/" + API_key + "/" + cities["Boston"] + "," + date).json()
    chicago = requests.get("https://api.forecast.io/forecast/" + API_key + "/" + cities["Chicago"] + "," + date).json()
    cleveland = requests.get("https://api.forecast.io/forecast/" + API_key + "/" + cities["Cleveland"]+ "," + date).json()
    cities_json = cities = {
        "Atlanta": atlanta,
            "Austin": austin,
            "Boston": boston,
            "Chicago": chicago,
            "Cleveland": cleveland
        }
    return cities_json

#create sqlite3 database
def connectToDatabase():
    con = lite.connect('weather.db')
    return con

#create my sqlite database table
def createSQLiteTable(con):
    # check to see if the database is created already
    # id_column = "id"
    # time_column = "Time"
    # city_column = "City"
    # max_temp =
    try:
        cur = con.cursor()
        with con:
            cur.execute('CREATE TABLE weather (id INT PRIMARY KEY, \
             city TEXT, max_temp INT, dateTaken TEXT)')
    # if created, return
    except lite.OperationalError:
        return

# update the SQLite table with the necessary variables
def updateSQLiteTable(cities_json, con, date):
    #fetching global ID to create unique ID's for the data points
    global unique_ID
    try:
        cur = con.cursor()
        sql = "INSERT INTO weather VALUES (?,?,?,?)"
        with con:
            for city in cities_json:
                cur.execute(sql,(unique_ID, city, cities_json[city]["daily"]["data"][0]["temperatureMax"], date))
                unique_ID += 1
    except lite.IntegrityError:
        return

#perform analysis on the weather data
def analysis(con):
    #dictionary to store data in
    cities_temp = {"Atlanta": [],
            "Austin": [],
            "Boston": [],
            "Chicago": [],
            "Cleveland": []}
    atlanta_temp = []
    austin_temp = []
    boston_temp = []
    chicago_temp = []
    cleveland_temp = []
    cur = con.cursor()
    with con:
        sqliteCommand = cur.execute('SELECT * FROM weather')
        for row in cur:
            if row[1] == "Atlanta":
                atlanta_temp.append(row[2])
            elif row[1] == "Austin":
                austin_temp.append(row[2])
            elif row[1] == "Boston":
                boston_temp.append(row[2])
            elif row[1] == "Chicago":
                chicago_temp.append(row[2])
            elif row[1] == "Cleveland":
                cleveland_temp.append(row[2])
        cities_temp["Atlanta"] = atlanta_temp
        cities_temp["Austin"] = austin_temp
        cities_temp["Boston"] = boston_temp
        cities_temp["Chicago"] = chicago_temp
        cities_temp["Cleveland"] = cleveland_temp

    # Which city had the greatest variation?
    variance_list = []
    variance_list.append(["Atlanta", np.var(cities_temp["Atlanta"])])
    variance_list.append(["Austin", np.var(cities_temp["Austin"])])
    variance_list.append(["Boston", np.var(cities_temp["Boston"])])
    variance_list.append(["Chicago", np.var(cities_temp["Chicago"])])
    variance_list.append(["Cleveland",np.var(cities_temp["Cleveland"])])
    max_variance = ["placeholder", 0]
    for i in range(len(variance_list)):
        if variance_list[i][1] >= max_variance[1]:
            max_variance = variance_list[i]
    print("The city with the greatest variation is {0}, with a variance of {1}".format(max_variance[0], max_variance[1]))


# What is the distribution of the difference?
    plt.figure()
    plt.hist(cities_temp.values(), histtype='bar')
    plt.show()

# Does the result surprise you? Why or why not?
# No they don't surprise me because Boston is a very cold city

def main():
    con = connectToDatabase()
    createSQLiteTable(con)
    cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }
    API_key = "fe97b4cef86991959b7c2a02a687e7d8"
    runs from day 1...30
    for i in range(1, 31):
        date = datetime.datetime.now() - datetime.timedelta(days=30-i)
        iso_format = date.isoformat()
        clean_date = iso_format.split(".")[0]
        # return a city json for the specific date
        cities_json = getData(API_key, cities, str(clean_date))
        # save max temp, city, date
        updateSQLiteTable(cities_json, con, clean_date)
        print(cities_json["Austin"]["daily"]["data"][0]["temperatureMax"])
        print(cities_json["Chicago"]["daily"]["data"][0]["temperatureMax"])
    analysis(con)
main()
