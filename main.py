from funcionario import funciones

# de inicio, la lista tiene valores (salvo que elimines todos los coches y sobrescribas el fichero).
"""
Esta es una aplicación (sencilla) de gestión de coches. Tiene los métodos básicos en mi opinión. 
Tiene para insertar un coche, buscar un coche, modificar un coche, eliminar un coche,
mostrar los coches de la lista y imprimir dicha lista en el fichero de coches.json.
"""

lista_coches: list = funciones.get_coches()
opcion = 0
print("GESTION DE COCHES\n")
# utilizo un while para realizar las operaciones y no salga hasta que el usuario quiera salir.
while opcion != 8:

    print(
        "1. Añadir Coche\n"
        "2. Consultar Coche\n"
        "3. Actualizar Coche\n"
        "4. Borrar Coche\n"
        "5. Mostrar Todos los Coches\n"
        "6. Filtrar Coches\n"
        "7. Imprimir en Fichero\n"
        "8. Salir\n"
    )

    opcion = int(input("Escribe una opcion a realizar:\n"))
    # manejo de errores por si fuera necesaria
    #if(opcion<1 and opcion>8):
       #raise clases.OptionNotExpected() no he conseguido que me funcionara, me salia antes incluso al iniciar la primera vez

    print()

    # en funcion de la opcion que le ponga (número int) realizará un metodo u otro.
    match (opcion):
        case 1:  # añadir coche.
            if funciones.insert_coches(lista_coches):
                print("Coche creado con exito.")
            else:
                print("error al insertar coche.")
            print()

        case 2:  # consultar coche.
            if funciones.search_coche(lista_coches) != None:
                print("El coche buscado existe.")
            else:
                print("el coche no existe en la lista")
            print()

        case 3:  # actualizar coche.
            if funciones.update_coche(lista_coches):
                print("El coche modificado con exito.")
            else:
                print("Error al modificar coche ergo no se ha modificado el coche.")
            print()
        case 4:  # borrar coche.
            if funciones.delete_coche(lista_coches):
                print("Coche eliminado con exito")
            else:
                print("Error al eliminar el coche")
            print()

        case 5:  # mostrar lista de coches.
            for coche in lista_coches:
                print(coche)
            print()

        case 6:  # ordenar por matricula.
            lista_ordenada = funciones.order_by_matricula(lista_coches)
            for coche in lista_ordenada:
                print(coche)
            print()

        case 7:  # volcar la lista de coches en el fichero de data.
            funciones.write_to_archive(lista_coches)
            print("fichero coches.json modificado con exito")
            print()

        case 8:  # sale del programa.
            print("Adios")
