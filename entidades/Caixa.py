#######################################################
# 
# Caixa.py
# Python implementation of the Class Caixa
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################


class Caixa:

    def __init__(self, saldo:float):
        self.__saldo = saldo

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo:float):
        self.__saldo = saldo