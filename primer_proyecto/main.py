from FunMat import FunMat
from Materia import Materia
from mysql_conection.conection import Connection
from funcionario import Funcionario

mi_con = Connection()
mi_con.connect()

"""
SQL_QUERY="SELECT * FROM Funcionario"

cursor = mi_con.connection.cursor()
cursor.execute(SQL_QUERY)

for row in cursor:
    print(row)

# Limpiar
cursor.close()
"""
funcionario = Funcionario(mi_con.connection)
# funcionario.create(10, 'Juan Pérez', 'Calle Falsa 123')

print(" LISTAR FUNCIONARIOS ")
print("  ")
funcionario.readAll()

materia = Materia(mi_con.connection)
#materia.update(2, "Algoritmos 1")
#materia.create(3, "Base de Datos 1")

#materia.delete(2)

print(" LISTAR MATERIAS ")
print("  ")
materia.readAll()


funmat= FunMat(mi_con.connection)
#funmat.create(1,1)
#nuevos_valores = {'id_funcionario': 1, 'id_materia ': 2}
#funmat.update(1, 1, nuevos_valores)
print(" LISTAR FUNMAT ")
print("  ")
funmat.readAll()


mi_con.disconnect()
