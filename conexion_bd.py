import psycopg2 

def connect_db():
    connection = psycopg2.connect(
        dbname="prog_avanzada",  
        user="postgres",         
        password="postgres",    
        host="localhost",           
        port="5432"                 
    )
    cursor = connection.cursor()
    return connection, cursor

def create_table():
    connection, cursor = connect_db()
    
    # Crear la tabla 'usuarios'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            edad INTEGER
        )
    ''')
    
    # Crear la tabla 'clientes'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100),
            ciudad VARCHAR(100)
        )
    ''')
    
    # Crear la tabla 'empleados'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id SERIAL PRIMARY KEY,
            salario INTEGER,
            puesto VARCHAR(100)
        )
    ''')
    
    # Crear la tabla 'pedidos'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id SERIAL PRIMARY KEY,
            cliente_id INTEGER REFERENCES clientes(id)
        )
    ''')
    
    # Crear la tabla 'ventas'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id SERIAL PRIMARY KEY,
            producto VARCHAR(100)
        )
    ''')

    connection.commit()
    connection.close()


# Insertar datos en la tabla 'usuarios'
def insert_data_usuarios(nombre, edad):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    connection.commit()
    connection.close()

# Insertar datos en la tabla 'empleados'
def insert_data_empleados(salario, puesto):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO empleados (salario, puesto) VALUES (%s, %s)", (salario, puesto))
    connection.commit()
    connection.close()
    

# Insertar datos en la tabla 'clientes'
def insert_data_clientes(nombre, ciudad):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO clientes (nombre, ciudad) VALUES (%s, %s)", (nombre, ciudad))
    connection.commit()
    connection.close()

# Insertar datos en la tabla 'pedidos'
def insert_data_pedidos(cliente_id):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO pedidos (cliente_id) VALUES (%s)", (cliente_id,))
    connection.commit()
    connection.close()

# Insertar datos en la tabla 'ventas'
def insert_data_ventas(producto):
    connection, cursor = connect_db()
    cursor.execute("INSERT INTO ventas (producto) VALUES (%s)", (producto,))
    connection.commit()
    connection.close()


# Consultar datos de la tabla
def query_data(query):
    connection, cursor = connect_db()
    rows = []
    try:
        cursor.execute(query)  
        connection.commit()    

        if query.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()

        print("Consulta ejecutada con éxito")
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        connection.close()  

    return rows
