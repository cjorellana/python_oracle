import cx_Oracle

class OracleDatabase:
    def __init__(self, host, port, service_name, user, password):
        
        dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
        self.conn = cx_Oracle.connect(user=user, password=password, dsn=dsn)
        self.cursor = self.conn.cursor()

    def listado_pais(self):
        stored_procedure = "begin sp_listar_pais(:1); end;"

        # Crear el parámetro de salida
        output = self.cursor.var(cx_Oracle.CURSOR)
        self.cursor.execute(stored_procedure, [output])
        result = output.getvalue()
        return result


    def execute_stored_procedure(self, v_pais_id, v_nombre, v_region):
        # Definir el procedimiento almacenado para ejecutar
        stored_procedure = "begin sp_agrega_pais(:1, :2, :3, :4); end;"

        # Crear la variable de salida
        v_salida = self.cursor.var(cx_Oracle.NUMBER)

        # Ejecutar el procedimiento almacenado
        self.cursor.execute(stored_procedure, [v_pais_id, v_nombre, v_region, v_salida])

        # Devolver el resultado
        return v_salida.getvalue()

    def close(self):
        self.cursor.close()
        self.conn.close()

# Usar la clase:
#db = OracleDatabase('localhost', '1521', 'XE', 'hr', 'hr')
#result = db.execute_stored_procedure('ID', 'Nombre', 1)
#print('Resultado:', result)
#db.close()