class Materia:
    def __init__(self, conn):
        self.conn = conn

    def create(self, id, nombre):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO materia (id, nombre) VALUES (?, ?)", (id, nombre))
        self.conn.commit()
        cursor.close()

    def read(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM materia WHERE id = ?", (id,))
        for row in cursor:
            print(row)
        cursor.close()

    def update(self, id, nombre):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE materia SET nombre = ? WHERE id = ?", (id, nombre))
        self.conn.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM materia WHERE id = ?", (id,))
        self.conn.commit()
        cursor.close()

    def readAll(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM materia")
        for row in cursor:
            print(row)
        cursor.close()


# El cursor es un intermediario entre mi códifo y la BD y permite
# ejecutar comandos de SQL a traves de metodo execute, manejar tx y consulas en BD, ademas cerrar la conexion'''
