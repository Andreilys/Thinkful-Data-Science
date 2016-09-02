import sqlite3 as lite
import pandas as pd

def connectToDatabase():
    con = lite.connect('database_Example.db')
    return con

# creates a table and stores values in it
def createTables(con):
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE cities (name text, state text)')
        cur.execute('CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)')
        cities = (('Las Vegas', 'NV'),
                            ('Atlanta', 'GA'), ('San Francisco', 'CA'),
                                                 ('Los Angeles', 'CA'), ('New York', 'NY'))

        weather = (('Las Vegas', 2013, 'July', 'December', 4),
                             ('Atlanta', 2013, 'July', 'January', 5), ('San Francisco', 2013, 'September', 'December', 4),
                                                   ('Los Angeles', 2013, 'September', 'January', 5), ('New York', 2013, 'July', 'February', 5))
        cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
        cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
        con.commit()
    except:
        return

#Joins the tables city and weather together to be stored in a dataframe object
def createDataFrame(con):
    with con:
        cur = con.cursor()
        rows = cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city")
        rows = cur.fetchall()
        cols = [desc[0] for desc in cur.description]
        df = pd.DataFrame(rows, columns=cols)
        return df

# takes in a dataframe object and figures out which cities are warmest in july
def warmestJulyCity(dataFrame):
    length = len(dataFrame.index)
    warmestCityString = "The cities that are warmest in July are: "
    for i in range(length):
        if str(dataFrame.get("warm_month")[i]) == "July":
            if i < length - 1:
                warmestCityString = warmestCityString + str(dataFrame.get("name")[i]) + ", "
            #make sure that the last addition doesn't have the comma
            else:
                warmestCityString = warmestCityString + str(dataFrame.get("name")[i])
    print(warmestCityString)

def main():
    con = connectToDatabase()
    createTables(con)
    dataFrame = createDataFrame(con)
    warmestJulyCity(dataFrame)

main()
