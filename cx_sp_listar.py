import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='hr', password='hr', dsn=dsn)

# Crear el cursor
cursor = conn.cursor()

# Definir el procedimiento almacenado para ejecutar
stored_procedure = "begin sp_listar_pais(:1); end;"

# Crear el parámetro de salida
output = cursor.var(cx_Oracle.CURSOR)

# Ejecutar el procedimiento almacenado
cursor.execute(stored_procedure, [output])

# Obtener los resultados
result = output.getvalue()

# Imprimir los resultados
for row in result:
    print(row)

# Cerrar la conexión
cursor.close()
conn.close()
