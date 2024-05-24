import pyodbc

class Funcionario:

    def __init__(self, conn):
        self.conn=conn

    def create(self, id, nombre, direccion):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO funcionario (id, nombre, direccion) VALUES (?, ?, ?)", (id, nombre, direccion))
        self.conn.commit()
        cursor.close()

    def read(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM funcionario WHERE id = ?", (id,))
        for row in cursor:
            print(row)
        cursor.close()

    def readAll(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM funcionario")
        for row in cursor:
            print(row)
        cursor.close()


    def update(self, id, nombre, direccion):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE funcionario SET nombre = ?, direccion = ? WHERE id = ?", (nombre, direccion, id))
        self.conn.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM funcionario WHERE id = ?", (id,))
        self.conn.commit()
        cursor.close()
