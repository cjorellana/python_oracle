from ora_db2 import OracleDatabase

db = OracleDatabase('localhost', 'XE', 'hr', 'hr')

region_id = '10'
result = db.listado_pais_x_region(region_id)

for row in result:
    print(row)

db.close()