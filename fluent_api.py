from conexion_bd import insert_data_empleados, insert_data_usuarios, insert_data_clientes, insert_data_pedidos, insert_data_ventas

class FluentQuery:
    def __init__(self):
        self.query = ""

    # Método para realizar una consulta SELECT
    def traeme(self, *args):
        self.query += f"TRAEME {', '.join(args)} "
        return self

    # Método para definir la tabla en la consulta
    def de_la_tabla(self, table_name):
        self.query += f"DE LA TABLA {table_name} "
        return self

    # Método para agregar la condición WHERE
    def donde(self, condition):
        self.query += f"DONDE {condition} "
        return self

    # Método para insertar datos en la tabla 'usuarios'
    def insert_usuarios(self, nombre, edad):
        insert_data_usuarios(nombre, edad)  # Usa la función insert_data para insertar en la base de datos
        return self
    
    # Método para insertar datos de la tabla 'empleados'
    def insert_empleados(self, salario, puesto):
        insert_data_empleados(salario, puesto)
        return self
    
    # Método para insertar datos de la tabla 'clientes'
    def insert_clientes(self, nombre, ciudad):
        insert_data_clientes(nombre, ciudad)
        return self
    
    # Método para insertar datos de la tabla 'pedidos'
    def insert_pedidos(self, cliente_id):
        insert_data_pedidos(cliente_id)
        return self
    
    # Método para insertar datos de la tabla 'ventas'
    def insert_ventas(self, producto):
        insert_data_ventas(producto)
        return self

    # Método para construir la consulta completa
    def build(self):
        return self.query.strip()
