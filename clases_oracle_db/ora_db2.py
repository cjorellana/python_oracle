import oracledb

class OracleDatabase:
    def __init__(self, host, service_name, user, password):
        
        dsn = f"{host}/{service_name}" 
        self.conn = oracledb.connect(user=user, password=password,dsn=dsn)
        self.cursor = self.conn.cursor()

    def listado_pais(self):
        stored_procedure = "sp_listar_pais"

        # Crear el parámetro de salida
        output = self.cursor.var(oracledb.CURSOR)
        self.cursor.callproc(stored_procedure, [output])
        result = output.getvalue()
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()