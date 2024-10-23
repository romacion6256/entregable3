import ply.yacc as yacc
from dsl_lexer import tokens  # Importar los tokens generados por el lexer
from coneccion_bd import query_data

# Regla para una consulta SELECT simple
def p_statement_select(t):
    '''statement : statement token
                 | token'''
    if len(t) == 3:  # Si hay más de un token, concatenar
        t[0] = t[1] + " " + t[2]
    else:
        t[0] = t[1]  # Si es solo un token, usarlo directamente

def p_token(t):
    '''token : WORD
              | NUMBER
              | GT
              | LT
              | EQ'''
    t[0] = str(t[1])  # Convertir el valor del token a cadena

# Manejo de errores
def p_error(t):
    print(f"Error sintáctico: {t}")

# Función que ejecuta la consulta
def execute_query(query):
    results = query_data(query)  # Llama a la función de la base de datos
    print("Resultados de la consulta:")
    if not results:
        print("No hay resultados")
        return
    for row in results:
        print(row)
        
def parse_input(data):
    # Procesar la entrada y generar la consulta SQL
    result = parser.parse(data)  # Analiza la consulta
    return result  # Devuelve el resultado (la consulta SQL generada)

parser = yacc.yacc()


