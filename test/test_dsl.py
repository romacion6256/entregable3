import unittest
from dsl_lexer import lex_input
from dsl_parser import parse_input, execute_query
from fluent_api import FluentQuery
from conexion_bd import (
    create_table, connect_db, insert_data_usuarios, 
    insert_data_empleados, insert_data_clientes, 
    insert_data_pedidos, insert_data_ventas, query_data
)

class TestConexionBD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_table()  

    def test_connect_db(self):
        connection, cursor = connect_db()
        self.assertIsNotNone(connection)
        self.assertIsNotNone(cursor)
        connection.close()

    def test_insert_data_usuarios(self):
        insert_data_usuarios("Carlos", 35)
        results = query_data("SELECT * FROM usuarios WHERE nombre = 'Carlos'")
        self.assertTrue(any("Carlos" in row for row in results))

    def test_insert_data_empleados(self):
        insert_data_empleados(2000, "ingeniero")
        results = query_data("SELECT * FROM empleados WHERE puesto = 'ingeniero'")
        self.assertTrue(any("ingeniero" in row for row in results))

    def test_insert_data_clientes(self):
        insert_data_clientes("Ana", "Montevideo")
        results = query_data("SELECT * FROM clientes WHERE ciudad = 'Montevideo'")
        self.assertTrue(any("Ana" in row for row in results))

    def test_insert_data_pedidos(self):
        insert_data_clientes("Cliente Pedido", "Ciudad")
        insert_data_pedidos(1)  
        results = query_data("SELECT * FROM pedidos WHERE cliente_id = 1")
        self.assertTrue(len(results) > 0)

    def test_insert_data_ventas(self):
        insert_data_ventas("ProductoX")
        results = query_data("SELECT * FROM ventas WHERE producto = 'ProductoX'")
        self.assertTrue(any("ProductoX" in row for row in results))



class TestLexer(unittest.TestCase):
    def test_lex_input(self):
        consulta = "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 25"
        tokens = lex_input(consulta)
        self.assertGreater(len(tokens), 0)
        self.assertEqual(tokens[0].value, "SELECT")  


class TestParser(unittest.TestCase):
    def test_parse_select(self):
        consulta = "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 25"
        sql_query = parse_input(consulta)
        self.assertEqual(sql_query.replace("  ", " ").strip(), "SELECT * FROM usuarios WHERE edad > 25")

    def test_parse_insert(self):
        consulta = "METE_EN usuarios (nombre, edad) LOS_VALORES ('Juan', 30)"
        sql_query = parse_input(consulta)
        expected_query = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 30)"
        self.assertEqual("".join(sql_query.split()), "".join(expected_query.split()))


    def test_invalid_query(self):
        consulta_invalida = "SELECTO TODO FROME usuarios"
        try:
            sql_query = parse_input(consulta_invalida)  
            execute_query(sql_query)
            self.fail("Se esperaba una excepción debido a una consulta inválida, pero no se lanzó ninguna.")
        except Exception as e:
            self.assertIn("consulta inválida", str(e))  




class TestFluentQuery(unittest.TestCase):

    def test_traeme_de_la_tabla_donde(self):
        query = FluentQuery().traeme("nombre", "edad").de_la_tabla("usuarios").donde("edad > 25").build()
        self.assertEqual(query, "TRAEME nombre, edad DE_LA_TABLA usuarios DONDE edad > 25")

    def test_agrupando_por(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").agrupando_por("ciudad").build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios AGRUPANDO_POR ciudad")

    def test_mezclando(self):
        query = FluentQuery().traeme("usuarios.nombre").mezclando("pedidos").build()
        self.assertEqual(query, "TRAEME usuarios.nombre MEZCLANDO pedidos")

    def test_en(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").en("Montevideo").build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios EN Montevideo")

    def test_los_distintos(self):
        query = FluentQuery().traeme("LOS_DISTINTOS nombre").de_la_tabla("usuarios").build()
        self.assertEqual(query, "TRAEME LOS_DISTINTOS nombre DE_LA_TABLA usuarios")

    def test_contando(self):
        query = FluentQuery().contando("nombre").de_la_tabla("usuarios").build()
        self.assertEqual(query, "CONTANDO nombre DE_LA_TABLA usuarios")

    def test_mete_en_los_valores(self):
        query = FluentQuery().mete_en("usuarios", "nombre", "edad").los_valores("'Carlos'", "35").build()
        self.assertEqual(query, "METE_EN usuarios (nombre, edad) LOS_VALORES ('Carlos', 35)")

    def test_actualiza_setea_donde(self):
        query = FluentQuery().actualiza("usuarios").setea("edad = 40").donde("nombre = 'Carlos'").build()
        self.assertEqual(query, "ACTUALIZA usuarios SETEA edad = 40 DONDE nombre = 'Carlos'")

    def test_borra_de_la_tabla(self):
        query = FluentQuery().borra_de_la_tabla("usuarios").donde("edad < 20").build()
        self.assertEqual(query, "BORRA_DE_LA_TABLA usuarios DONDE edad < 20")

    def test_ordena_por(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").ordena_por("edad").como_mucho(10).build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios ORDENA_POR edad COMO_MUCHO 10")

    def test_where_del_group_by(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").where_del_group_by().build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios WHERE_DEL_GROUP_BY")

    def test_existe(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").existe().build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios EXISTE")

    def test_en_esto(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").en_esto("otra_tabla").build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios EN_ESTO otra_tabla")

    def test_entre(self):
        query = FluentQuery().traeme("edad").de_la_tabla("usuarios").entre(20, 30).build()
        self.assertEqual(query, "TRAEME edad DE_LA_TABLA usuarios ENTRE 20 AND 30")

    def test_parecido_a(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").parecido_a("'Car%'").build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios PARECIDO_A 'Car%'")

    def test_es_nulo(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").donde("apellido").es_nulo().build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios DONDE apellido ES_NULO")

    def test_cambia_la_tabla_agrega_la_columna(self):
        query = FluentQuery().cambia_la_tabla("usuarios").agrega_la_columna("edad", "INT").build()
        self.assertEqual(query, "CAMBIA_LA_TABLA usuarios AGREGA_LA_COLUMNA edad INT")

    def test_crea_la_tabla(self):
        query = FluentQuery().crea_la_tabla("usuarios").build()
        self.assertEqual(query, "CREA_LA_TABLA usuarios")

    def test_por_defecto_unico(self):
        query = FluentQuery().traeme("nombre").por_defecto("'Sin nombre'").unico().build()
        self.assertEqual(query, "TRAEME nombre POR_DEFECTO 'Sin nombre' UNICO")

    def test_clave_prima_clave_referente(self):
        query = FluentQuery().traeme("id").clave_prima().clave_referente("id", "clientes", "cliente_id").build()
        self.assertEqual(query, "TRAEME id CLAVE_PRIMA CLAVE_REFERENTE (id) clientes (cliente_id)")

    def test_no_nulo_y_transforma_a(self):
        query = FluentQuery().traeme("nombre").no_nulo().y().transforma_a("VARCHAR(50)").build()
        self.assertEqual(query, "TRAEME nombre NO_NULO Y TRANSFORMA_A VARCHAR(50)")
    def test_donde_and_entre(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").donde("edad").entre(20, 30).build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios DONDE edad ENTRE 20 AND 30")

    def test_existe_and_es_nulo(self):
        query = FluentQuery().traeme("nombre").de_la_tabla("usuarios").donde("nombre").existe().y().es_nulo().build()
        self.assertEqual(query, "TRAEME nombre DE_LA_TABLA usuarios DONDE nombre EXISTE Y ES_NULO")

    def test_elimina_la_columna(self):
        query = FluentQuery().cambia_la_tabla("usuarios").elimina_la_columna("edad").build()
        self.assertEqual(query, "CAMBIA_LA_TABLA usuarios ELIMINA_LA_COLUMNA edad")

    def test_tira_la_tabla(self):
        query = FluentQuery().tira_la_tabla("usuarios").build()
        self.assertEqual(query, "TIRA_LA_TABLA usuarios")

    def test_por_defecto(self):
        query = FluentQuery().crea_la_tabla("usuarios").agrega_la_columna("nombre", "VARCHAR").por_defecto("'Desconocido'").build()
        self.assertEqual(query, "CREA_LA_TABLA usuarios AGREGA_LA_COLUMNA nombre VARCHAR POR_DEFECTO 'Desconocido'")

    def test_unico_and_clave_prima(self):
        query = FluentQuery().crea_la_tabla("usuarios").agrega_la_columna("id", "INT").unico().clave_prima().build()
        self.assertEqual(query, "CREA_LA_TABLA usuarios AGREGA_LA_COLUMNA id INT UNICO CLAVE_PRIMA")

    def test_clave_referente(self):
        query = FluentQuery().crea_la_tabla("usuarios").clave_referente("id", "clientes", "cliente_id").build()
        self.assertEqual(query, "CREA_LA_TABLA usuarios CLAVE_REFERENTE (id) clientes (cliente_id)")

    def test_transforma_a(self):
        query = FluentQuery().cambia_la_tabla("usuarios").transforma_a("BIGINT").build()
        self.assertEqual(query, "CAMBIA_LA_TABLA usuarios TRANSFORMA_A BIGINT")
    
    def test_los_distintos(self):
        query = FluentQuery().los_distintos("nombre", "edad").de_la_tabla("usuarios").build()
        self.assertEqual(query, "LOS_DISTINTOS nombre, edad DE_LA_TABLA usuarios")

    def test_insert_usuarios(self):
        FluentQuery().insert_usuarios("Pedro", 28)
        results = query_data("SELECT * FROM usuarios WHERE nombre = 'Pedro' AND edad = 28")
        self.assertTrue(any("Pedro" in row for row in results))

    def test_insert_empleados(self):
      
        FluentQuery().insert_empleados(3000, "developer")
        results = query_data("SELECT * FROM empleados WHERE puesto = 'developer' AND salario = 3000")
        self.assertTrue(any("developer" in row for row in results))

    def test_insert_clientes(self):
       
        FluentQuery().insert_clientes("Maria", "Madrid")
        results = query_data("SELECT * FROM clientes WHERE nombre = 'Maria' AND ciudad = 'Madrid'")
        self.assertTrue(any("Maria" in row for row in results))

    def test_insert_pedidos(self):
        
        FluentQuery().insert_clientes("ClientePedido", "Ciudad")
        FluentQuery().insert_pedidos(1)  
        results = query_data("SELECT * FROM pedidos WHERE cliente_id = 1")
        self.assertTrue(len(results) > 0)

    def test_insert_ventas(self):
        FluentQuery().insert_ventas("ProductoY")
        results = query_data("SELECT * FROM ventas WHERE producto = 'ProductoY'")
        self.assertTrue(any("ProductoY" in row for row in results))

    


class TestMainFunctionality(unittest.TestCase):
    def test_execute_query_select(self):
        consulta = "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 25"
        sql_query = parse_input(consulta)
        results = execute_query(sql_query)
        self.assertIsInstance(results, list)  

    def test_execute_query_insert(self):
        consulta = "METE_EN usuarios (nombre, edad) LOS_VALORES ('Luis', 32)"
        sql_query = parse_input(consulta)
        result = execute_query(sql_query)
        results = query_data("SELECT * FROM usuarios WHERE nombre = 'Luis'")
        self.assertTrue(any("Luis" in row for row in results))  

    def test_execute_query_update(self):
        consulta = "ACTUALIZA usuarios SETEA edad = 40 DONDE nombre = 'Luis'"
        sql_query = parse_input(consulta)
        execute_query(sql_query)
        results = query_data("SELECT * FROM usuarios WHERE nombre = 'Luis'")
        self.assertTrue(any(row[2] == 40 for row in results))  


if __name__ == "__main__":
    unittest.main()