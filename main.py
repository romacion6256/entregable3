from dsl_lexer import lex_input
from dsl_parser import execute_query, parse_input
from coneccion_bd import create_table
from fluent_api import FluentQuery

if __name__ == "__main__":
    # Crear la tabla en la base de datos si no existe
    create_table()

    # Ejemplo de consulta USQL que será traducida a SQL y ejecutada en la base de datos
    consulta_usql = (input("Ingrese la consulta USQL: "))
    
    print("Lexing...")
    tokens = lex_input(consulta_usql)
    # for token in tokens:
    #     print(token)

    print("Parsing y ejecución...")
    print(f'Ejecutando consulta: {consulta_usql}')
    consulta_a_sql = parse_input(consulta_usql)
    execute_query(consulta_a_sql)
    
    # También puedes usar la Fluent API para interactuar con la base de datos
    #fluent = FluentQuery()
    #fluent.insert("Juan", 40)  # Inserta datos a la tabla 'usuarios'
    #fluent.consultar()           # Consulta todos los datos de la tabla 'usuarios'
