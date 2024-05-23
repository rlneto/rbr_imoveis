#######################################################
# 
# DAOPlataforma.py
# Python implementation of the Class DAOPlataforma
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
import os, pickle
from DAOs.DAO import DAO
from entidades.Plataforma import Plataforma


class DAOPlataforma(DAO):
    def __init__(self, arquivo: str):
        self.__arquivo = arquivo
        self._DAOPlataforma__conteudo = []
        if os.path.exists(self.__arquivo):
            try:
                self._DAOPlataforma__conteudo = self.__load()
            except FileNotFoundError:
                self.__dump()
                self.__load()

    @property
    def conteudo(self) -> list[Plataforma]:
        return self._DAOPlataforma__conteudo

    @conteudo.setter
    def conteudo(self, valor: list[Plataforma]):
        self._DAOPlataforma__conteudo = valor

    def create(self, desc: str, titulo: str, id: int, habilitado=True) -> bool:
        tamanho = len(self.conteudo)
        self.conteudo.append(Plataforma(desc=desc, titulo=titulo, ident=id, habilitado=habilitado))
        self.__dump()
        self.__load()
        if len(self.conteudo) > tamanho:
            return True
        else:
            return False

    def delete(self, id: int) -> bool:
        for i in range(len(self.conteudo)):
            if self.conteudo[i].id == id:
                self.conteudo[i].habilitado = False
                self.__dump()
                self.__load()
                return True
        return False

    def read(self) -> list:
        return [plataforma for plataforma in self.conteudo if plataforma.habilitado]

    def update(self, id: int, novo_titulo: str, nova_desc: str) -> bool:
        for i in range(len(self.conteudo)):
            if self.conteudo[i].id == id:
                self.conteudo[i].titulo = novo_titulo
                self.conteudo[i].desc = nova_desc
                self.__dump()
                self.__load()
                return True
        return False

    def __dump(self):
        with open(self.__arquivo, 'wb') as arquivo:
            pickle.dump(self.conteudo, arquivo)

    def __load(self):
        with open(self.__arquivo, 'rb') as arquivo:
            self.conteudo = pickle.load(arquivo)
        return self.conteudo
