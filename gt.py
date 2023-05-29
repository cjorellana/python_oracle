import oracledb
import os

un = 'hr'
pw = 'hr'
cs = 'localhost:1521/XE'

with oracledb.connect(user=un, password=pw,dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = "insert into COUNTRIES(COUNTRY_ID,COUNTRY_NAME,REGION_ID)"
        sql += "values (:1, :2, :3)"
        cursor.execute(sql,('GT', "GUATEMALA",10))
        connection.commit()