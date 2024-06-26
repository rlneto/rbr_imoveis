#######################################################
# 
# ContadorReceita.py
# Python implementation of the Class ContadorReceita
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from entidades.Contador import Contador

class ContadorReceita(Contador):
    def __init__(self):
        self.__valor = 400000

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor