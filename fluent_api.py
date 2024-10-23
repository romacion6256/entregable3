from coneccion_bd import insert_data, query_data

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

    # Método para insertar datos en la tabla
    def insert(self, nombre, edad):
        insert_data(nombre, edad)  # Usa la función insert_data para insertar en la base de datos
        return self

    # Método para consultar datos de la tabla
    def consultar(self):
        results = query_data()  # Usa la función query_data para obtener los datos de la base de datos
        for row in results:
            print(row)
        return self

    # Método para construir la consulta completa
    def build(self):
        return self.query.strip()
