import ply.yacc as yacc
from dsl_lexer import tokens  # Importar los tokens generados por el lexer
from conexion_bd import query_data

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
              | EQ
              | STRING
              | LPAREN
              | RPAREN
              | COMMA
              | ASTERISK
              | DOT'''
    t[0] = str(t[1])  # Convertir el valor del token a cadena

# Manejo de errores
def p_error(t):
    print(f"Error sintáctico: {t}")

def execute_query(query):
    results = query_data(query)  
    print("Resultados de la consulta:")
    if not results:
        print("No hay resultados")
        return [] 
    for row in results:
        print(row)
    return results  

        
def parse_input(data):
    try:
        result = parser.parse(data)  
        return result  
    except Exception as e:
        raise Exception("Error al analizar la consulta SQL: consulta inválida") from e

parser = yacc.yacc()
