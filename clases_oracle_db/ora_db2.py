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
    
    def listado_pais_x_region(self,p_region_id):
        stored_procedure = "SEL_PAIS_X_REGION"
        
        # Crear el parámetro de salida
        retval = self.cursor.var(oracledb.CURSOR)

        self.cursor.callproc(stored_procedure, [p_region_id, retval])
        result = retval.getvalue().fetchall()
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()