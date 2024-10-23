import psycopg2

# Conectar a la base de datos PostgreSQL
def connect_db():
    connection = psycopg2.connect(
        dbname="prog_avanzada",  # Nombre de tu base de datos
        user="postgres",          # Usuario de tu base de datos
        password="postgres",    # Contraseña del usuario
        host="localhost",           # Host de tu base de datos (en este caso, local)
        port="5432"                 # Puerto por defecto de PostgreSQL
    )
    cursor = connection.cursor()
    return connection, cursor

# Crear una tabla en la base de datos
def create_table():
    connection, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            edad INTEGER
        )
    ''')
    connection.commit()
    connection.close()

# Insertar datos en la tabla
def insert_data(nombre, edad):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    connection.commit()
    connection.close()

# Consultar datos de la tabla
def query_data():
    connection, cursor = connect_db()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    connection.close()
    return rows
