import oracledb
import os

un = 'hr'
pw = 'hr'
cs = 'localhost:1521/XE'

with oracledb.connect(user=un, password=pw,dsn=cs) as connection:
    cursor = connection.cursor()
    for row in cursor.execute("select * from COUNTRIES"):
        print(row)