#######################################################
# 
# ControladorSenha.py
# Python implementation of the Class ControladorSenha
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from limites.TelaVerificaSenha import TelaVerificaSenha
from limites.TelaAlteraSenha import TelaAlteraSenha
from DAOs.DAOSenha import DAOSenha


class ControladorSenha:

    def __init__(self):
        self.__dao = DAOSenha("./senha.pkl")

    def verificar_senha(self):
        tela = TelaVerificaSenha()
        senha = tela.verifica_senha()
        return self.__dao.read() == senha

    def alterar_senha(self):
        tela = TelaAlteraSenha()
        senha = tela.altera_senha()
        if senha is not None:
            self.__dao.update(senha)
            return True
        return False

    def erro_senha(self):
        tela = TelaVerificaSenha()
        tela.mostra_popup("Senha incorreta!")

