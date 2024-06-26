#######################################################
# 
# DAOContadorSaque.py
# Python implementation of the Class DAOContadorSaque
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
import os, pickle
from DAOs.DAO import DAO
from entidades.ContadorSaque import ContadorSaque

class DAOContadorSaque(DAO):
    def __init__(self, arquivo: str):
        self.__arquivo = arquivo
        self._DAOContadorSaque__conteudo = []
        try:
            self._DAOContadorSaque__conteudo = self.__load()
        except FileNotFoundError:
            self._DAOContadorSaque__conteudo.append(ContadorSaque())
            self.__dump()
            self.__load()

    @property
    def conteudo(self):
        return self._DAOContadorSaque__conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        self._DAOContadorSaque__conteudo = conteudo
        
    def read(self) -> int:
        return self.conteudo[0].valor

    def update(self):
        self.conteudo[0].valor += 1
        self.__dump()
        self.__load()
        return self.conteudo[0].valor

    def __dump(self):
        with open(self.__arquivo, 'wb') as arquivo:
            pickle.dump(self.conteudo, arquivo)

    def __load(self):
        with open(self.__arquivo, 'rb') as arquivo:
            self.conteudo = pickle.load(arquivo)
        return self.conteudo