class FunMat:
    def __init__(self, conn):
        self.conn = conn

    def create(self, id_fun, id_mat):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO funmat (id_funcionario, id_materia) VALUES (?, ?)", (id_fun, id_mat))
        self.conn.commit()
        cursor.close()

    def read(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM funmat WHERE id_funcionario= ? and id_materia= ? ", (id,))
        for row in cursor:
            print(row)
        cursor.close()

    def update(self, id_fun, id_mat, nuevos_valores):
        cursor = self.conn.cursor()
        query = """UPDATE funmat SET id_funcionario = ?, id_materia = ? 
                   WHERE id_funcionario = ? AND id_materia = ?"""
        cursor.execute(query, (nuevos_valores['id_funcionario'], nuevos_valores['id_materia'], id_fun, id_mat))
        self.conn.commit()
        cursor.close()

    def readAll(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM funmat")
        for row in cursor:
            print(row)
        cursor.close()
