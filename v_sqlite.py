import sqlite3 as lite
import pandas as pd

cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 4),
                     ('Atlanta', 2013, 'July', 'January', 5))

con = lite.connect('getting_started.db')

# Inserting rows by passing tuples to `execute()`
with con:
    cur = con.cursor()
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
    cur.execute("SELECT * FROM weather")
    rows = cur.fetchall()

    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns = cols)
    print(df)
