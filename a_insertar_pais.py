from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', '1521', service_name='XE')

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user="hr",
    password="hr",
    sid=dsn
)

engine =  create_engine(
    cstr,
    pool_recycle=10,
    pool_size=50,
    echo=True
)

# Asume que tu tabla COUNTRIES tiene las columnas COUNTRY_ID y COUNTRY_NAME
new_country_id = 'CO'
new_country_name = 'Colombia'
new_region_id = 10

# Crea una nueva conexión
connection = engine.connect()

try:
    # Inicia una nueva transacción
    trans = connection.begin()

    # Prepara tu consulta de inserción
    query = text("INSERT INTO COUNTRIES (COUNTRY_ID, COUNTRY_NAME, REGION_ID) VALUES (:country_id, :country_name, :region_id)")

    # Ejecuta la consulta de inserción con los valores que deseas insertar
    connection.execute(query, {"country_id": new_country_id, "country_name": new_country_name, "region_id": new_region_id})

    # Si todo sale bien, confirma la transacción
    trans.commit()
except SQLAlchemyError as e:
    # Si ocurre un error, haz un rollback de la transacción
    trans.rollback()
    print(f"Error al insertar en la base de datos: {str(e)}")
finally:
    # Asegúrate de cerrar la conexión
    connection.close()
