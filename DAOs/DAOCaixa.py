#######################################################
# 
# DAOCaixa.py
# Python implementation of the Class DAOCaixa
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
import os, pickle
from entidades.Caixa import Caixa
from DAOs.DAO import DAO


class DAOCaixa(DAO):
    def __init__(self, arquivo: str):
        self.__arquivo = arquivo
        if os.path.exists(self.__arquivo):
            self.__conteudo = pickle.load(open(self.__arquivo, "rb"))
        else:
            self.__conteudo = [Caixa(0)]

    @property
    def conteudo(self):
        return self.__conteudo

    def create(self):
        pass

    def delete(self):
        pass

    def read(self):
        return self.conteudo[0].saldo


    def update(self, novo_saldo: float):
        self.conteudo[0].saldo = novo_saldo
        pickle.dump(self.conteudo, open(self.__arquivo, "wb"))