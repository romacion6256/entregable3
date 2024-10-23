import ply.yacc as yacc
from dsl_lexer import tokens  # Importar los tokens generados por el lexer
from coneccion_bd import query_data

# Regla para una consulta SELECT simple
def p_statement_select(t):
    '''statement : WORD WORD WORD WORD'''
    sql_query = " ".join(t[1:])  # Construir la consulta SQL
    print(f'Traduciendo a SQL: {sql_query}')
    execute_query(sql_query)

# Manejo de errores
def p_error(t):
    print(f"Error sintáctico: {t}")

# Función que ejecuta la consulta
def execute_query(query):
    print(f'Ejecutando consulta: {query}')
    results = query_data()  # Llama a la función de la base de datos
    for row in results:
        print(row)
        
def parse_input(data):
    parser.parse(data)
# Inicializa el parser
parser = yacc.yacc()


