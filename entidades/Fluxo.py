#######################################################
# 
# Fluxo.py
# Python implementation of the Class Fluxo
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from abc import ABC, abstractmethod
from datetime import date
class Fluxo(ABC):
    @abstractmethod
    def __init__(self, ident: int, obs: str, valor: float, data: str):
        self.__id = ident
        self.__obs = obs
        self.__valor = valor
        self.__data = data

    # def __repr__(self):
    #     return f"Data: {self.__data} - Valor: {self.__valor} - Observação: {self.__obs} - Id:{self.__id}"

    @property
    def obs(self) -> str:
        return self.__obs

    @obs.setter
    def obs(self, obs:str):
        self.__obs = obs

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor:float):
        self.__valor = valor

    @property
    def id(self) -> int:
        return self.__id

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data:date):
        self.__data = data