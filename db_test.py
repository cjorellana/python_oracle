import oracledb
import os

un = 'hr'
pw = 'hr'
cs = 'localhost:1521/XE'



with oracledb.connect(user=un, password=pw,dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select sysdate from dual"""
        for r in cursor.execute(sql):
            print(r)

