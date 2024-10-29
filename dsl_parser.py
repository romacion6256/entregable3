import ply.yacc as yacc
from dsl_lexer import tokens  # Importar los tokens generados por el lexer
from conexion_bd import query_data
from conexion_bd import connect_db


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

# Función que ejecuta la consulta
def execute_query(query):
    connection, cursor = connect_db()
    try:
        cursor.execute(query)
        connection.commit()
        if query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            return results if results is not None else []  # Asegura retorno de lista
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        raise
    finally:
        connection.close()

        
def parse_input(data):
    # Procesar la entrada y generar la consulta SQL
    result = parser.parse(data)  # Analiza la consulta
    return result  # Devuelve el resultado (la consulta SQL generada)

parser = yacc.yacc()


