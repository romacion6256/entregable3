import ply.lex as lex

# Diccionario completo de traducción de USQL a SQL
usql_to_sql = {
"SELECT": "TRAEME",
"*": "TODO",
"FROM": "DE LA TABLA",
"WHERE": "DONDE",
"GROUP BY": "AGRUPANDO POR",
"JOIN": "MEZCLANDO",
"ON": "EN",
"DISTINCT": "LOS DISTINTOS",
"COUNT": "CONTANDO",
"INSERT INTO": "METE EN",
"VALUES": "LOS VALORES",
"UPDATE": "ACTUALIZA",
"SET": "SETEA",
"DELETE FROM":
"BORRA DE LA",
"ORDER BY": "ORDENA POR",
"LIMIT": "COMO MUCHO",
"HAVING": "WHERE DEL GROUP BY",
"EXISTS": "EXISTE",
"IN": "EN ESTO:",
"BETWEEN": "ENTRE",
"LIKE": "PARECIDO A",
"IS NULL": "ES NULO",
"ALTER TABLE": "CAMBIA LA TABLA",
"ADD COLUMN": "AGREGA LA COLUMNA",
"DROP COLUMN": "ELIMINA LA COLUMNA",
"CREATE TABLE": "CREA LA TABLA",
"DROP TABLE": "TIRA LA TABLA",
"DEFAULT": "POR DEFECTO",
"UNIQUE": "UNICO",
"PRIMARY KEY": "CLAVE PRIMA",
"FOREIGN KEY": "CLAVE REFERENTE",
"NOT NULL": "NO NULO",
"CAST": "TRANSFORMA A",
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
