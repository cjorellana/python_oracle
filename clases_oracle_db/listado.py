from ora_db2 import OracleDatabase

# Usar la clase:
#db = OracleDatabase('localhost', '1521', 'XE', 'hr', 'hr')
#result = db.execute_stored_procedure('ID', 'Nombre', 1)
#print('Resultado:', result)
#db.close()

# listar
db = OracleDatabase('localhost', 'XE', 'hr', 'hr')
result = db.listado_pais()
for row in result:
    print(row)

db.close()