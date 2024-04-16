#######################################################
# 
# Imovel.py
# Python implementation of the Class Imovel
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################


class Imovel:
    def __init__(self, desc: str, ident: int, titulo: str, habilitado=True):
        self.__desc = desc
        self.__id = ident
        self.__titulo = titulo
        self.__habilitado = habilitado

    def __repr__(self):
        return f"Título: {self.__titulo} - Descrição: {self.__desc}"

    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def id(self) -> int:
        return self.__id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def habilitado(self) -> bool:
        return self.__habilitado

    @habilitado.setter
    def habilitado(self, habilitado: bool):
        self.__habilitado = habilitado
