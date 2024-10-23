import ply.lex as lex

# Diccionario completo de traducción de USQL a SQL
usql_to_sql = {
    "TRAEME": "SELECT",
    "TODO": "*",
    "DE LA TABLA": "FROM",
    "DONDE": "WHERE",
    "AGRUPANDO POR": "GROUP BY",
    "MEZCLANDO": "JOIN",
    "EN": "ON",
    "LOS DISTINTOS": "DISTINCT",
    "CONTANDO": "COUNT",
    "METE EN": "INSERT INTO",
    "LOS VALORES": "VALUES",
    "ACTUALIZA": "UPDATE",
    "SETEA": "SET",
    "BORRA DE LA": "DELETE FROM",
    "ORDENA POR": "ORDER BY",
    "COMO MUCHO": "LIMIT",
    "WHERE DEL GROUP BY": "HAVING",
    "EXISTE": "EXISTS",
    "EN ESTO:": "IN",
    "ENTRE": "BETWEEN",
    "PARECIDO A": "LIKE",
    "ES NULO": "IS NULL",
    "ALTERA LA TABLA": "ALTER TABLE",
    "AGREGA LA COLUMNA": "ADD COLUMN",
    "ELIMINA LA COLUMNA": "DROP COLUMN",
    "CREA LA TABLA": "CREATE TABLE",
    "TIRA LA TABLA": "DROP TABLE",
    "POR DEFECTO": "DEFAULT",
    "UNICO": "UNIQUE",
    "CLAVE PRIMA": "PRIMARY KEY",
    "CLAVE REFERENTE": "FOREIGN KEY",
    "NO NULO": "NOT NULL",
    "TRANSFORMA A": "CAST"
}

# Agregamos tokens para operadores
tokens = ['WORD', 'GT', 'LT', 'EQ']

t_ignore = ' \t'

# Definimos tokens para operadores
t_GT = r'>'
t_LT = r'<'
t_EQ = r'='

# Definir cómo identificar palabras clave y convertirlas de USQL a SQL
def t_WORD(t):
    r'\w+'
    t.type = 'WORD'
    if t.value.upper() in usql_to_sql:
        t.value = usql_to_sql[t.value.upper()]  # Convierte USQL a SQL
    return t

def t_error(t):
    print(f"Error léxico: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Función para procesar el input
def lex_input(data):
    lexer.input(data)
    return list(lexer)
