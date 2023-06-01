from sqlalchemy import create_engine, text
import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', '1521', service_name='XE')

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user="hr",
    password="hr",
    sid=dsn
)

# Crea el motor de SQLAlchemy usando cx_Oracle
engine =  create_engine(
    cstr,
    pool_recycle=10,
    pool_size=50,
    echo=True
)


with engine.connect() as connection:
    result = connection.execute(text('select COUNTRY_NAME from COUNTRIES'))


for row in result:
    print(row)

