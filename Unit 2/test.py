Dictionary = {"hello" : []}

Dictionary["hello"] = 5
Dictionary["hello"].append(10)

print(Dictionary)


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

# Which city had the greatest variation?
austin_diff = max(austin_temp) - min(austin_temp)
atlanta_diff = max(atlanta_temp) - min(atlanta_temp)
boston_diff = max(boston_temp) - min(boston_temp)
chicago_diff = max(chicago_temp) - min(chicago_temp)
cleveland_diff = max(cleveland_temp) - min(cleveland_temp)

print(max(austin_diff, atlanta_diff, boston_diff, chicago_diff, cleveland_diff))
print("The city that had the most differnce was {0}".format(austin_diff))

# print(weather_data[1][2])
