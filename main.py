from dsl_lexer import lex_input
from dsl_parser import parse_input
from coneccion_bd import create_table

if __name__ == "__main__":
    # Crear la tabla en la base de datos si no existe
    create_table()

    # Ejemplo de consulta USQL que será traducida a SQL y ejecutada en la base de datos
    consulta_usql = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 25"
    
    print("Lexing...")
    tokens = lex_input(consulta_usql)
    for token in tokens:
        print(token)

    print("\nParsing y ejecución...")
    parse_input(consulta_usql)

    # También puedes usar la Fluent API para interactuar con la base de datos
    #fluent = FluentQuery()
    #fluent.insert("Francisco", 50)  # Inserta datos a la tabla 'usuarios'
    #fluent.consultar()           # Consulta todos los datos de la tabla 'usuarios'
