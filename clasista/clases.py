class Coche:
    # hago los atributos privados añadiendo __ delante de cada uno para obligarme a utilizar los geter y seter
    __matricula: str
    __marca: str
    __modelo: str

    def __init__(self, matricula: str, marca: str, modelo: str):
        self.__matricula = matricula
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self) -> str:
        return f"{self.__matricula}, {self.__marca}, {self.__modelo}"

    def get_matricula(self) -> str:
        return f"{self.__matricula}"

    def get_marca(self) -> str:
        return f"{self.__marca}"

    def get_modelo(self) -> str:
        return f"{self.__modelo}"

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

# creo una excepcion propia para comprobar si escribo la opcion correcta
#class OptionNotExpected(Exception):
    #print("La opcion no es valida. Ha de ser entre el 1 y el 8.")