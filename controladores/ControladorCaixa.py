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

class ControladorCaixa:

    def __init__(self):
        self.__dao_caixa = DAOCaixa("caixa.pkl")
        self.__caixa = self.__dao_caixa.read()

    def atualizar_caixa(self, despesas:list, receitas:list, aportes:list, saques:list):
        total = 0
        for despesa in despesas:
            total -= despesa.valor
        for receita in receitas:
            total += receita.valor
        for aporte in aportes:
            total += aporte.valor
        for saque in saques:
            total -= saque.valor
        self.__dao_caixa.update(total)

    @property
    def caixa(self):
        return self.__caixa
