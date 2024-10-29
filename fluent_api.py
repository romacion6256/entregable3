from conexion_bd import insert_data_empleados, insert_data_usuarios, insert_data_clientes, insert_data_pedidos, insert_data_ventas

class FluentQuery:
    def __init__(self):
        self.query = ""

    def traeme(self, *args):
        self.query += f"TRAEME {', '.join(args)} "
        return self

    def de_la_tabla(self, table_name):
        self.query += f"DE_LA_TABLA {table_name} "
        return self

    def donde(self, condition):
        self.query += f"DONDE {condition} "
        return self

    def agrupando_por(self, *args):
        self.query += f"AGRUPANDO_POR {', '.join(args)} "
        return self
    
    def mezclando(self, table_name):    
        self.query += f"MEZCLANDO {table_name} "
        return self
    
    def en(self, condition):
        self.query += f"EN {condition} "
        return self
    
    def los_distintos(self, *args):
        self.query += f"LOS_DISTINTOS {', '.join(args)} "
        return self
    
    def contando(self, *args):
        self.query += f"CONTANDO {', '.join(args)} "
        return self
    
    def mete_en(self, table_name, *args):
        self.query += f"METE_EN {table_name} ({', '.join(args)}) "
        return self
    
    def los_valores(self, *args):
        self.query += f"LOS_VALORES ({', '.join(args)}) "
        return self
    
    def actualiza(self, table_name):
        self.query += f"ACTUALIZA {table_name} "
        return self
    
    def setea(self, condition):
        self.query += f"SETEA {condition} "
        return self
    
    def borra_de_la_tabla(self, table_name):
        self.query += f"BORRA_DE_LA_TABLA {table_name} "
        return self
    
    def ordena_por(self, *args):
        self.query += f"ORDENA_POR {', '.join(args)} "
        return self
    
    def como_mucho(self, limit):
        self.query += f"COMO_MUCHO {limit} "
        return self
    
    def where_del_group_by(self):
        self.query += f"WHERE_DEL_GROUP_BY  "
        return self
    
    def existe(self):
        self.query += f"EXISTE "
        return self
    
    def en_esto(self, condition):
        self.query += f"EN_ESTO {condition} "
        return self
    
    def entre(self, condition1, condition2):
        self.query += f"ENTRE {condition1} AND {condition2} "
        return self
    
    def parecido_a(self, condition):
        self.query += f"PARECIDO_A {condition} "
        return self
    
    def es_nulo(self):  
        self.query += f"ES_NULO "
        return self
    
    def cambia_la_tabla(self, table_name):
        self.query += f"CAMBIA_LA_TABLA {table_name} "
        return self
    
    def agrega_la_columna(self, column_name, data_type):
        self.query += f"AGREGA_LA_COLUMNA {column_name} {data_type} "
        return self
    
    def elimina_la_columna(self, column_name):
        self.query += f"ELIMINA_LA_COLUMNA {column_name} "
        return self
    
    def crea_la_tabla(self, table_name):
        self.query += f"CREA_LA_TABLA {table_name} "
        return self
    
    def tira_la_tabla(self, table_name):
        self.query += f"TIRA_LA_TABLA {table_name} "
        return self
    
    def por_defecto(self, value):
        self.query += f"POR_DEFECTO {value} "
        return self
    
    def unico(self):
        self.query += f"UNICO "
        return self
    
    def clave_prima(self):
        self.query += f"CLAVE_PRIMA "
        return self 

    def clave_referente(self, column_name, table_name, column_name2):
        self.query += f"CLAVE_REFERENTE ({column_name}) {table_name} ({column_name2}) "
        return self
    
    def no_nulo(self):
        self.query += f"NO_NULO "
        return self
    
    def transforma_a(self, data_type):
        self.query += f"TRANSFORMA_A {data_type} "
        return self
    
    def y(self):
        self.query += f"Y "
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
