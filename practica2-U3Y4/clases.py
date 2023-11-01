from datetime import *
from abc import ABC, abstractmethod, abstractclassmethod

class Estadia():
    vehiculos_estadia = []
    def __init__(self, __fecha: date, __nro_patente: str, __hora_entrada: time, __hora_salida: time, __cant_horas: int, __estado: str, __pagado:bool) -> None:
        self.__fecha = __fecha
        self.__nro_patente = __nro_patente # {unique}
        self.__hora_entrada = __hora_entrada
        self.__hora_salida = __hora_salida
        self.__cant_horas = __cant_horas # /
        self.__estado = __estado
        self.__pagado = __pagado
    
    @property   
    def get_fecha(self):
        return datetime.today()
    @property    
    def set_fecha(self, nuevo_fecha):
        if isinstance(nuevo_fecha, date):
            self.__fecha = nuevo_fecha
        else:
            print("La fecha debe ser del tipo date.")
    
    @property    
    def get_nro_patente(self):
        return self.__nro_patente
    @property    
    def set_nro_patente(self, nuevo_nro_patente):
        if isinstance(nuevo_nro_patente, str):
            self.__nro_patente = nuevo_nro_patente
        else:
            print("El numero debe ser una cadena de caracteres.")
            
    @property    
    def get_hora_entrada(self):
        return datetime.now()
    @property    
    def set_hora_entrada(self, nuevo_hora_entrada):
        if isinstance(nuevo_hora_entrada, time):
            self.__hora_entrada = nuevo_hora_entrada
        else:
            print("La hora de entrada debe ser del tipo time.")
    
    @property    
    def get_hora_salida(self):
        return self.__hora_salida
    @get_hora_salida.setter    
    def set_hora_salida(self, nuevo_hora_salida):
        if isinstance(nuevo_hora_salida, time):
            self.__hora_salida = nuevo_hora_salida
        else:
            print("La hora de salida debe ser del tipo time.")
    
    @property    
    def get_cant_horas(self):
        return self.__cant_horas
    @property    
    def set_cant_horas(self, nuevo_cant_horas):
        if isinstance(nuevo_cant_horas, int):
            self.__cant_horas = nuevo_cant_horas
        else:
            print("La cantidad de horas debe ser del tipo time.")
    
    @property    
    def get_estado(self):
        self.__estado = "ACTIVO"
        return self.__estado
    @get_estado.setter   
    def set_estado(self, nuevo_estado):
        if isinstance(nuevo_estado, str):
            self.__estado = nuevo_estado
        else:
            print("El estado debe ser una cadena de caracteres.")
            
    @property    
    def get_pagado(self):
        self.__pagado = False
        return self.__pagado
    @property    
    def set_pagado(self, nuevo_pagado):
        if isinstance(nuevo_pagado, bool):
            self.__pagado = nuevo_pagado
        else:
            print("El pagado debe ser del tipo booleano.")
    
    def __str__(self) -> str:
        return f""" Fecha:{self.__fecha}
                    Nro. patente: {self.__nro_patente}
                    Hora de entrada: {self.__hora_entrada}
                    Hora de salida: {self.__hora_salida}
                    Cantidad de horas: {self.__cant_horas}
                    Estado: {self.__estado}
                    Pagado: {self.__pagado}"""
    
    def registrar_salida():
        pass
    
class Precio():
    __precio_hora = 10
    
    @abstractclassmethod
    def calcular_importe(cls, get_cant_horas) -> None:

        return Precio.__precio_hora*get_cant_horas 


