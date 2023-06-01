import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', '1521', service_name='XE')
conn = cx_Oracle.connect(user='hr', password='hr', dsn=dsn)

# Crear el cursor
cursor = conn.cursor()

# Definir el procedimiento almacenado para ejecutar
stored_procedure = "begin sp_agrega_pais(:1, :2, :3, :4); end;"

# Definir los valores de entrada
v_pais_id = 'HD'
v_nombre = 'Honduras'
v_region = 10

# Crear la variable de salida
v_salida = cursor.var(cx_Oracle.NUMBER)

# Ejecutar el procedimiento almacenado
cursor.execute(stored_procedure, [v_pais_id, v_nombre, v_region, v_salida])

# Imprimir el resultado
print('Resultado:', v_salida.getvalue())

# Cerrar la conexión
cursor.close()
conn.close()
