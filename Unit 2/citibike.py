import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as lite
import time
from dateutil.parser import parse
import collections

# get data from citibike NYC
def getData():
    r = requests.get('http://www.citibikenyc.com/stations/json')
    json_data = r.json()
    return json_data

# get the keylist from the JSON data
def getKeyList(json_data):
    key_list = []
    for station in json_data['stationBeanList']:
        for k in station.keys():
            if k not in key_list:
                key_list.append(k)
    return key_list

# create the pandas dataframe
def createDataFrame(json_data):
    df = json_normalize(json_data['stationBeanList'])
    return df

def createSQLiteTable():
    # check to see if the database is created already
    try:
        con = lite.connect("citi_bike.db")
        cur = con.cursor()
        with con:
            cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, \
            totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude \
            NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, \
            landMark TEXT, latitude NUMERIC, location TEXT )')
    # if created, return
    except lite.OperationalError:
        return

# update the SQLite table with the necessary variables
def updateSQLiteTable(json_data):
    #connect to DB and update values
    try:
        con = lite.connect("citi_bike.db")
        cur = con.cursor()
        sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, \
        longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) \
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

        with con:
            for station in json_data['stationBeanList']:
                  cur.execute(sql,(station['id'],station['totalDocks'],station['city'],\
                  station['altitude'],station['stAddress2'],station['longitude'],\
                  station['postalCode'],station['testStation'],station['stAddress1'],\
                  station['stationName'],station['landMark'],station['latitude'],\
                  station['location']))
    # if values already updated with citibike_reference then return
    except lite.IntegrityError:
        return

def createAvailableBikesTable(df):
    try:
        con = lite.connect("citi_bike.db")
        cur = con.cursor()
        station_ids = df['id'].tolist()
        station_ids = ['_' + str(x) + ' INT' for x in station_ids]

        with con:
            cur.execute("CREATE TABLE available_bikes ( execution_time INT, " + \
             ", ".join(station_ids) + ");")

    except lite.OperationalError:
        return

def updateExecutionTime(json_data):
    con = lite.connect("citi_bike.db")
    cur = con.cursor()
    exec_time = parse(json_data['executionTime'])
    with con:
        cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
    id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

    #loop through the stations in the station list
    for station in json_data['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']

    #iterate through the defaultdict to update the values in the database
    with con:
        for k, v in id_bikes.iteritems():
            cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + \
            " WHERE execution_time = " + exec_time.strftime('%s') + ";")


def main():
    json_data = getData()
    key_list = getKeyList(json_data)
    df = createDataFrame(json_data)
    # if created returns 1, then upload data
    createSQLiteTable()
    updateSQLiteTable(json_data)
    createAvailableBikesTable(df)
    updateExecutionTime(json_data)
for i in range(60):
    main()
    time.sleep(60)  # Delay for 1 minute (60 seconds)
