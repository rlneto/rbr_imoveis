#######################################################
# 
# ControladorAportes.py
# Python implementation of the Class ControladorAportes
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from limites.TelaAportes import TelaAportes
from DAOs.DAOAporte import DAOAporte
from controladores.ControladorGeraIdAporte import ControladorGeraIdAporte

class ControladorAportes:
 
    C_APORTES = "C_APORTES"
    R_APORTES = "R_APORTES"                
    D_APORTES = "D_APORTES"
    APORTES = "APORTES"
    VOLTAR = "VOLTAR"

    def __init__(self):
        self.__dao = DAOAporte("aportes.pkl")
        self.__tela = TelaAportes()

    @property
    def dao(self):
        return self.__dao

    def abrir_menu(self):
        while True:
            escolha = self.__tela.abrir_menu()
            if escolha is None or escolha == self.VOLTAR:
                return
            elif escolha == self.C_APORTES:
                self.cadastrar_aporte()
            elif escolha == self.R_APORTES:
                self.listar_aportes()
            elif escolha == self.D_APORTES:
                self.excluir_aporte()
    
    def cadastrar_aporte(self):
        valor, obs, data = self.__tela.cadastrar_aporte()
        if valor is None and obs is None and data is None:
            return

        if self.validar_campos_vazios(valor, obs, data):
            return
        
        if not self.validar_valor(valor):
            return

        id = ControladorGeraIdAporte().gera_id()
        self.__dao.create(id, valor=valor, data=data, obs=obs)

    def excluir_aporte(self):
        aporte = self.__dao.read()
        if not aporte:
            self.__tela.mostra_popup("Não há aportes cadastrados.")
            return

        id_aportes = self.__tela.excluir_aportes(aporte)
        if id_aportes is None:
            return
        
        if not self.validar_id(id_aportes):
            return
        
        self.__dao.delete(int(id_aportes))

    def listar_aportes(self):
        aportes = self.__dao.read()
        if not aportes:
            self.__tela.mostra_popup("Não há aportes cadastrados.")
        else:
            self.__tela.exibir_aportes(aportes)

    def validar_campos_vazios(self, valor, obs, data):
        if (valor is None or obs is None or data is None or
            valor.strip() == "" or obs.strip() == "" or data.strip() == ""):
            self.__tela.mostra_popup("Todos os campos devem ser preenchidos.")
            return True
        return False

    def validar_valor(self, valor):
        try:
            valor = float(valor)
            if valor <= 0:
                self.__tela.mostra_popup("O valor do aporte deve ser um número maior que zero.")
                return False
            return True
        except ValueError:
            self.__tela.mostra_popup("O valor do aporte deve ser um número.")
            return False

    def validar_id(self, id_aporte):
        if not id_aporte.strip():
            self.__tela.mostra_popup("O campo ID não pode estar vazio.")
            return False

        try:
            id_aporte = int(id_aporte)
        except ValueError:
            self.__tela.mostra_popup("O ID do aporte deve ser um número inteiro.")
            return False

        if not any(aporte.id == id_aporte for aporte in self.__dao.read()):
            self.__tela.mostra_popup(f"Aporte com ID {id_aporte} não encontrado.")
            return False

        return True