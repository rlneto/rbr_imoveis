#######################################################
# 
# DAOAporte.py
# Python implementation of the Class DAOAporte
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
import os, pickle
from DAOs.DAO import DAO
from entidades.Aporte import Aporte

class DAOAporte(DAO):
    def __init__(self, arquivo: str):
        self.__arquivo = arquivo
        self._DAOAporte__conteudo = []
        if os.path.exists(self.__arquivo):
            try:
                self._DAOAporte__conteudo = self.__load()
            except FileNotFoundError:
                self.__dump()
                self.__load()


    @property
    def conteudo(self) -> list:
        return self._DAOAporte__conteudo
    
    @conteudo.setter
    def conteudo(self, valor: list):
        self._DAOAporte__conteudo = valor

    def create(self, id: int, obs: str, valor: float, data: str) -> bool: 
        tamanho = len(self.conteudo)
        novo_aporte = Aporte(ident=id, obs=obs, valor=valor, data=data)
        self.conteudo.append(novo_aporte)
        self.__dump()
        self.__load()
        if len(self.conteudo) > tamanho:
            return True
        else:
            return False

    def delete(self, id: int) -> bool:
        for i in range(len(self.conteudo)):
            if self.conteudo[i].id == id:
                del self.conteudo[i]
                self.__dump()
                self.__load()
                return True
        return False

    def read(self) -> list:
        return [aporte for aporte in self.conteudo]

    def __dump(self):
        with open(self.__arquivo, 'wb') as arquivo:
            pickle.dump(self.conteudo, arquivo)

    def __load(self):
        with open(self.__arquivo, 'rb') as arquivo:
            self.conteudo = pickle.load(arquivo)
        return self.conteudo