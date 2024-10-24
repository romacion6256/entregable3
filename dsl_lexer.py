import ply.lex as lex

# Diccionario de traducción de USQL a SQL
usql_to_sql = {
    "TRAEME": "SELECT",
    "TODO": "*",
    "DE_LA_TABLA": "FROM",
    "DONDE": "WHERE",
    "AGRUPANDO_POR": "GROUP BY",
    "MEZCLANDO": "JOIN",
    "EN": "ON",
    "LOS_DISTINTOS": "DISTINCT",
    "CONTANDO": "COUNT",
    "METE_EN": "INSERT INTO",
    "LOS_VALORES": "VALUES",
    "ACTUALIZA": "UPDATE",
    "SETEA": "SET",
    "BORRA_DE_LA_TABLA": "DELETE FROM",
    "ORDENA_POR": "ORDER BY",
    "COMO_MUCHO": "LIMIT",
    "WHERE_DEL_GROUP_BY": "HAVING",
    "EXISTE": "EXISTS",
    "EN_ESTO:": "IN",
    "ENTRE": "BETWEEN",
    "PARECIDO_A": "LIKE",
    "ES_NULO": "IS NULL",
    "CAMBIA_LA_TABLA": "ALTER TABLE",
    "AGREGA_LA_COLUMNA": "ADD COLUMN",
    "ELIMINA_LA_COLUMNA": "DROP COLUMN",
    "CREA_LA_TABLA": "CREATE TABLE",
    "TIRA_LA_TABLA": "DROP TABLE",
    "POR_DEFECTO": "DEFAULT",
    "UNICO": "UNIQUE",
    "CLAVE_PRIMA": "PRIMARY KEY",
    "CLAVE_REFERENTE": "FOREIGN KEY",
    "NO_NULO": "NOT NULL",
    "TRANSFORMA_A": "CAST",
    "Y": "AND",
}

# Definición de tokens
tokens = ['WORD', 'GT', 'LT', 'EQ', 'NUMBER', 'STRING', 'LPAREN', 'RPAREN', 'COMMA', 'ASTERISK', 'DOT']

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Definición de tokens para operadores
t_GT = r'>'
t_LT = r'<'
t_EQ = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ASTERISK = r'\*'
t_DOT = r'\.'

# Definición de números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Definición de cadenas de texto
def t_STRING(t):
    r'\'[^\']*\''
    t.value = str(t.value) # Remover las comillas
    return t

# Definición de WORD
def t_WORD(t):
    r'\w+'  # Captura palabras individuales
    # Si está en el diccionario, convertimos
    if t.value.upper() in usql_to_sql:
        t.value = usql_to_sql[t.value.upper()]  # Convierte palabras de USQL a SQL
    else:
        t.type = 'WORD'  # Aseguramos que sea tipo WORD si no está en el diccionario
    return t

def t_error(t):
    print(f"Error léxico: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

# Función para procesar el input
def lex_input(data):
    lexer.input(data)
    return list(lexer)
