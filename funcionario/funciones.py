import io
import json
from clasista import clases


def get_coches():
    coches: dict = []
    nombreFichero = "./practica12/la_trama/coches.json"
    lista_coches: list = []
    with open(nombreFichero, "r") as fichero:
        contenido = fichero.read()
        # vuelco el contenido del fichero al diccionario ya que es del tipo 'clave' : 'valor'.
        coches = json.loads(contenido)
        
        for car in coches:
            # vuelco el contenido del diccionario a una clase Coche.
            coche = clases.Coche(car["matricula"], car["marca"], car["modelo"])
            # dicho coche lo inserto a la lista (es más fácil trabajar para mi).
            lista_coches.append(coche)

        fichero.close()

    if lista_coches.__len__ == 0:
        print("no hay datos en la lista")

    return lista_coches


def insert_coches(lista_coches) -> bool:
    # recogo la lista de coches.
    # creo una lista con los valores que he escrito.
    lista = get_params_coche(3)
    matricula: str = lista[0]
    marca: str = lista[1]
    modelo: str = lista[2]

    coche = clases.Coche(matricula, marca, modelo)
    lista_coches.append(coche)
    return coche != None


# lo que retorno de aqui es un coche
def search_coche(lista_coches) -> clases.Coche:
    # aquí lo que me devuelve la función "get_params_coche" es una lista con solo un campo (el de matrícula).
    matricula: str = get_params_coche(1)[0]
    # ¿¿¿¿POR QUÉ NO EXISTE NULL EN PYTHON????
    searched_coche = None

    for coche in lista_coches:
        # de la lista compruebo si la matrícula del coche es la misma que la de la matrícula pasada.
        if coche.get_matricula().equals(matricula):
            searched_coche = coche
    # en caso positivo, me devolvera un coche, en caso contrario me devolverá un ...mmm un None.
    return searched_coche


def update_coche(lista_coches) -> bool:
    # aquí selecciono el coche que quiero utilizar.
    coche = select_to_do(lista_coches)
    # guardo el coche en su estado anterior
    pre_coche = coche
    # recogo los parametros que pido por consola.
    lista = get_params_coche(3)
    confirm: int = int(input("¿Seguro que quiere modificar el coche?\nSi=1, No=0\n"))
    if confirm == 1:
        matricula: str = lista[0]
        marca: str = lista[1]
        modelo: str = lista[2]

        # modifico el coche con los valores pasados.
        coche.set_matricula(matricula)
        coche.set_marca(marca)
        coche.set_modelo(modelo)

        # retorno si hay modificación en alguno de los campos o no.
    return coche != pre_coche


def delete_coche(lista_coches) -> bool:
    # selecciono el coche de la lista
    coche = select_to_do(lista_coches)
    confirm: int = int(input("¿Seguro que quiere borrar el coche?\nSi=1, No=0\n"))
    if confirm == 1:
        lista_coches.remove(coche)
        return True

    return False


# en esta funcion, ordeno el array de coches mediate la funcion sorter y le paso una lamba para que ordene la lista mediante las matriculas de los coches.
def order_by_matricula(lista_coches) -> list:
    # utilizo la funcion lambda que ordene la lista en funcion de la matricula.
    lista_filtrada = sorted(lista_coches, key=lambda coche: coche.get_matricula())

    return lista_filtrada


def get_params_coche(num: int) -> list:
    lista: list = []
    match (num):
        case 1: # en caso de que solo sea un parámetro, pregunto la matrícula y la devuelvo en una lista.
            matricula: str = input("Escriba la matricula del coche\n")
            lista.append(matricula)

        case 2: # en caso de que sean dos parámetros, pregunto la matrícula y la marca y las devuelvo en una lista.
            matricula: str = input("Escriba la matricula del coche\n")
            marca: str = input("Escriba la marca del coche\n")
            lista.append(matricula)
            lista.append(marca)

        case 3: # en caso de que sean tres parámetros, pregunto la matrícula y la marca y el modelo y las devuelvo en una lista.
            matricula: str = input("Escriba la matricula del coche\n")
            marca: str = input("Escriba la marca del coche\n")
            modelo: str = input("Escriba el modelo del coche\n")
            lista.append(matricula)
            lista.append(marca)
            lista.append(modelo)

    return lista


def select_to_do(lista_coches) -> clases.Coche:
    cont_coche = 1 # contador para poder seleccionar mas facilmente la el coche (en vez de poner el coche).
    for coche in lista_coches:
        print(cont_coche, coche)
        print()
        cont_coche += 1
    n: int = int(input("Escriba el numero del coche que quieras modificar.\n"))
    return lista_coches[(n - 1)] # necesito restarle uno porque las listas empiezan en 0.


def write_to_archive(lista_coches):
    diccionario_coches = list_to_dict(lista_coches) # la funcion me devuelve de la lista, un diccionario.
    nombreFichero = "./practica12/la_trama/coches.json"
    with open(nombreFichero, "w") as fichero:
        fichero.write(json.dumps(diccionario_coches)) # utilizo rl json para escribirlo como un fichero json y sobrescribir dicho fichero.
        fichero.close()


def list_to_dict(lista_coches) -> dict:
    diccionario_coches: dict = []

    # recorro el array de listas.
    for coche in lista_coches:
        diccionario_coches.append(
            {
                "matricula": coche.get_matricula(),
                "marca": coche.get_marca(),
                "modelo": coche.get_modelo(),
            }
        )
    return diccionario_coches
