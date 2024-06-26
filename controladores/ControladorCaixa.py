#######################################################
# 
# ControladorCaixa.py
# Python implementation of the Class ControladorCaixa
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from DAOs.DAOCaixa import DAOCaixa
from limites.TelaCaixa import TelaCaixa

class ControladorCaixa:

    def __init__(self, receitas, saques, despesas, aportes):
        self.__dao_caixa = DAOCaixa("caixa.pkl")
        self.__caixa = self.__dao_caixa
        self.__tela = TelaCaixa()
        self.__receitas = receitas
        self.__saques = saques
        self.__despesas = despesas
        self.__aportes = aportes

    @property
    def despesas(self):
        return self.__despesas

    @property
    def receitas(self):
        return self.__receitas

    @property
    def saques(self):
        return self.__saques

    @property
    def aportes(self):
        return self.__aportes

    def atualizar_caixa(self, despesas:list, receitas:list, saques:list, aportes:list):
        total = 0
        if isinstance(despesas, list):
            for despesa in despesas:
                total -= float(despesa.valor)
        if isinstance(receitas, list):
            for receita in receitas:
                total += float(receita.valor)
        if isinstance(saques, list):
            for saque in saques:
                total -= float(saque.valor)
        if isinstance(aportes, list):
            for aporte in aportes:
                total += float(aporte.valor)
        self.__dao_caixa.update(total)

    def exibir_caixa(self, despesas:list, receitas:list, saques:list, aportes:list):
        self.atualizar_caixa(despesas, receitas, saques, aportes)
        self.__tela.exibir_caixa(self.__caixa.read())


    @property
    def caixa(self):
        return self.__caixa

    @property
    def tela(self):
        return self.__tela

    def oi(self):
        return self.caixa.read()