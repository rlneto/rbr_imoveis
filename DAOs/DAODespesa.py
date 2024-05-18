#######################################################
# 
# DAODespesa.py
# Python implementation of the Class DAODespesa
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
import os, pickle
from DAOs.DAO import DAO
from entidades.Despesa import Despesa

class DAODespesa(DAO):
    def __init__(self, arquivo: str):
        self.__arquivo = arquivo
        self._DAODespesa__conteudo = []
        if os.path.exists(self.__arquivo):
            try:
                self._DAODespesa__conteudo = self.__load()
            except FileNotFoundError:
                self.__dump()
                self.__load()

    @property
    def conteudo(self) -> list:
        return self._DAODespesa__conteudo

    @conteudo.setter
    def conteudo(self, valor: list):
        self._DAODespesa__conteudo = valor

    def create(self):
        pass

    def delete(self):
        pass

    def read(self):
        pass