from math import sqrt


class ExceptionDatos(Exception):
    pass


class Estadistica:

    def __init__(self, numeros):
        self.__numeros = self.validarNumeros(numeros)

    def validarNumeros(self, numeros):
        if numeros is not None:
            for numero in numeros:
                if not isinstance(numero, int) and not isinstance(numero, float):
                    raise ValueError
            return numeros
        else:
            raise ExceptionDatos

    @property
    def numeros(self):
        return self.__numeros

    @numeros.setter
    def numeros(self, numeros):
        try:
            self.__numeros = self.validarNumeros(numeros)
        except ValueError as e:
            self.__numeros = []

    def desviacion_estandar(self):
        media = self.calcular_media()
        suma = 0
        for valor in self.__numeros:
            suma += (valor - media) ** 2
        radicando = suma / (len(self.__numeros))
        return sqrt(radicando)

    def calcular_media(self):
        if len(self.__numeros) > 0:
            suma = 0
            for valor in self.__numeros:
                suma += valor
            return suma / len(self.__numeros)
        else:
            raise ExceptionDatos
