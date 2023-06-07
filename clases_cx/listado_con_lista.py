from ora_db import OracleDatabase

# lista
lista = []

# listar
db = OracleDatabase('localhost', '1521', 'XE', 'hr', 'hr')
result = db.listado_pais()
for row in result:
    lista.append(row)
    #print(row)

db.close()

#print(type(lista))

for fila in lista:
    print(fila[0])