from dsl_lexer import lex_input
from dsl_parser import execute_query, parse_input
from conexion_bd import create_table
from fluent_api import FluentQuery

if __name__ == "__main__":
    
    # Crear la tabla en la base de datos si no existe
    create_table()

    # DESCOMENTAR LOS SIGUIENTES EJEMPLOS PARA INSERTAR DATOS EN LA BASE DE DATOS. UNA VEZ QUE SE EJECUTEN, COMENTARLOS DE NUEVO PARA EVITAR DUPLICADOS

    # También puedes usar la Fluent API para interactuar con la base de datos
    # fluent = FluentQuery()
    # fluent.insert_usuarios("Juan", 40)  # Inserta datos a la tabla 'usuarios'
    # fluent.insert_usuarios("María", 30)
    # fluent.insert_usuarios("Pedro", 25)        # Consulta todos los datos de la tabla 'usuarios'

    # fluent.insert_empleados(2000, "Gerente")  # Inserta datos a la tabla 'empleados'
    # fluent.insert_empleados(1500, "Asistente")
    # fluent.insert_empleados(1000, "Secretaria")

    # fluent.insert_clientes("Ana", "CDMX")  # Inserta datos a la tabla 'clientes'
    # fluent.insert_clientes("Luis", "Guadalajara")
    # fluent.insert_clientes("Sofía", "Monterrey")    

    # fluent.insert_pedidos(1)  # Inserta datos a la tabla 'pedidos'  
    # fluent.insert_pedidos(2)
    # fluent.insert_pedidos(3)

    # fluent.insert_ventas("Laptop")  # Inserta datos a la tabla 'ventas'
    # fluent.insert_ventas("Smartphone")  
    # fluent.insert_ventas("Tablet")
    
    while True:

        # Ejemplo de consulta USQL que será traducida a SQL y ejecutada en la base de datos
        consulta_usql = (input("Ingrese la consulta USQL: "))
        
        print("Lexing...")
        tokens = lex_input(consulta_usql)
        # for token in tokens:
        #     print(token)

        print("Parsing y ejecución...")
        consulta_a_sql = parse_input(consulta_usql)
        print(f'Consulta en SQL: {consulta_a_sql}')
        execute_query(consulta_a_sql) 