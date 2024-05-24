import pyodbc
class Connection:


    def __init__(self):
        self.host = "localhost"
        self.database = "comosellamatubasededatos"
        self.user = "elusuarioquecreaste"
        self.password = "lapassword"
        self.connection = None


    def connect(self):
        try:
            connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.host};DATABASE={self.database};UID={self.user};PWD={self.password}'
            self.connection = pyodbc.connect(connectionString)
            print("Conexión exitosa")
        except Exception as e:
            print("Error al conectar a la base de datos", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")



"""
SERVER = ''
DATABASE = ''
USERNAME = ''
PASSWORD = ''

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

SQL_QUERY = "SELECT * FROM Funcionario"


cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(f"{r.id}\t{r.nombre}\t{r.direccion}")
    
    
"""