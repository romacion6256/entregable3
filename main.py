from dsl_lexer import lex_input
from dsl_parser import execute_query, parse_input
from conexion_bd import create_table
from fluent_api import FluentQuery

if __name__ == "__main__":
    
    # Crear la tabla en la base de datos si no existe
    create_table()

    # DESCOMENTAR LOS SIGUIENTES EJEMPLOS PARA INSERTAR VALORES EN LA BASE DE DATOS. UNA VEZ QUE SE EJECUTEN, COMENTARLOS DE NUEVO PARA EVITAR DUPLICADOS

    # fluent = FluentQuery()
    # fluent.insert_usuarios("Juan", 30)  # Inserta datos a la tabla 'usuarios'
    # fluent.insert_usuarios("María", 15)
    # fluent.insert_usuarios("Pedro", 40)      

    # fluent.insert_empleados(2000, "ingeniero")  # Inserta datos a la tabla 'empleados'
    # fluent.insert_empleados(1500, "ingeniero")
    # fluent.insert_empleados(1000, "secretaria")

    # fluent.insert_clientes("Ana", "Madrid")  # Inserta datos a la tabla 'clientes'
    # fluent.insert_clientes("Luis", "Barcelona")
    # fluent.insert_clientes("Sofía", "Barcelona")    

    # fluent.insert_pedidos(1)  # Inserta datos a la tabla 'pedidos'  
    # fluent.insert_pedidos(2)
    # fluent.insert_pedidos(3)

    # fluent.insert_ventas("Laptop")  # Inserta datos a la tabla 'ventas'
    # fluent.insert_ventas("Smartphone")  
    # fluent.insert_ventas("Tablet")
    # fluent.insert_ventas("Tablet")
    # fluent.insert_ventas("Tablet")
    # fluent.insert_ventas("Tablet")
    # fluent.insert_ventas("Tablet")
    # fluent.insert_ventas("Tablet")
    
    ######################################################################################################################
    # CONSULTAS DE LA LETRA (DESCOMENTAR LA QUE SE QUIERA PROBAR Y COMENTAR LAS DEMÁS PARA EVITAR CONFLICTOS DE EJECUCIÓN)

    # Consulta para obtener todos los datos de la tabla 'usuarios'
    # consulta_usql_api= FluentQuery().traeme("TODO").de_la_tabla("usuarios").donde("edad > 25").build()
    # consulta_a_sql = parse_input(consulta_usql_api)
    # print(f'Consulta en SQL: {consulta_a_sql}')
    # execute_query(consulta_a_sql)

    # Consulta para obtener los nombres de los clientes de la ciudad de Monterrey
    # consulta_usql_api1= FluentQuery().traeme().los_distintos("nombre").de_la_tabla("clientes").donde("ciudad = 'Madrid'").build()
    # consulta_a_sql1 = parse_input(consulta_usql_api1)
    # print(f'Consulta en SQL: {consulta_a_sql1}')
    # execute_query(consulta_a_sql1)

    # Consulta para insertar datos en la tabla 'usuarios'   
    # consulta_usql_api2= FluentQuery().mete_en("usuarios", "nombre", "edad").los_valores("'Juan'", "25").build()
    # consulta_a_sql2 = parse_input(consulta_usql_api2)
    # print(f'Consulta en SQL: {consulta_a_sql2}')
    # execute_query(consulta_a_sql2)  

    # Consulta para actualizar el salario de los empleados con puesto 'Gerente'
    # consulta_usql_api3= FluentQuery().actualiza("empleados").setea("salario = 3000").donde("puesto = 'ingeniero'").build()
    # consulta_a_sql3 = parse_input(consulta_usql_api3)
    # print(f'Consulta en SQL: {consulta_a_sql3}')
    # execute_query(consulta_a_sql3)  

    # Consulta para obtener todo de un join entre las tablas 'pedidos' y 'clientes'
    # consulta_usql_api4= FluentQuery().traeme("TODO").de_la_tabla("pedidos").mezclando("clientes").en("pedidos.cliente_id= clientes.id").donde("clientes.ciudad = 'Barcelona'").build()
    # consulta_a_sql4 = parse_input(consulta_usql_api4)
    # print(f'Consulta en SQL: {consulta_a_sql4}')
    # execute_query(consulta_a_sql4)

    # Consulta para obtener la cantidad de registros agrupados por 'producto' en la tabla 'ventas'
    # consulta_usql_api5= FluentQuery().traeme().contando("(TODO)").de_la_tabla("ventas").agrupando_por("producto").where_del_group_by().contando("(TODO) > 5").build()
    # consulta_a_sql5 = parse_input(consulta_usql_api5)
    # print(f'Consulta en SQL: {consulta_a_sql5}')
    # execute_query(consulta_a_sql5)  

    # Consulta para borrar los registros de la tabla 'usuarios' donde la edad esté entre 18 y 25
    # consulta_usql_api6= FluentQuery().borra_de_la_tabla("usuarios").donde("edad").entre("18", "25").build()
    # consulta_a_sql6 = parse_input(consulta_usql_api6)
    # print(f'Consulta en SQL: {consulta_a_sql6}')
    # execute_query(consulta_a_sql6)

    # Consulta para agregar una columna 'direccion' a la tabla 'empleados'
    # consulta_usql_api7= FluentQuery().cambia_la_tabla("empleados").agrega_la_columna("direccion", "VARCHAR(255)").build()
    # consulta_a_sql7 = parse_input(consulta_usql_api7)
    # print(f'Consulta en SQL: {consulta_a_sql7}')
    # execute_query(consulta_a_sql7)

    # Consulta para eliminar la columna 'direccion' de la tabla 'empleados'
    # consulta_usql_api8= FluentQuery().cambia_la_tabla("empleados").elimina_la_columna("direccion").build()
    # consulta_a_sql8 = parse_input(consulta_usql_api8)
    # print(f'Consulta en SQL: {consulta_a_sql8}')
    # execute_query(consulta_a_sql8)
    
    while True:

        # Ejemplo de consulta USQL que será traducida a SQL y ejecutada en la base de datos
        consulta_usql = (input("Ingrese la consulta USQL: "))

        print("Lexing...")
        tokens = lex_input(consulta_usql)
        # for token in tokens:
        #     print(token)

        print("Parsing y ejecución...")
        consulta_a_sql = parse_input(consulta_usql)
        print(f'Consulta en SQL: {consulta_a_sql}')
        execute_query(consulta_a_sql) 