import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='hr', password='hr', dsn=dsn)

# Crear el cursor
cursor = conn.cursor()

# Ejecutar la consulta
cursor.execute('select sysdate from dual')

# Recorrer los resultados
for row in cursor:
    print(row)

# Cerrar la conexión
cursor.close()
conn.close()
