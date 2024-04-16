#######################################################
# 
# ControladorSistema.py
# Python implementation of the Class ControladorSistema
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from controladores.ControladorReceitas import ControladorReceitas
from controladores.ControladorMenu import ControladorMenu
from controladores.ControladorSenha import ControladorSenha
from controladores.ControladorDespesas import ControladorDespesas
from controladores.ControladorSaques import ControladorSaques
from controladores.ControladorAportes import ControladorAportes
from controladores.ControladorRelatorios import ControladorRelatorios
from controladores.ControladorPlataformas import ControladorPlataformas
from controladores.ControladorImoveis import ControladorImoveis
from controladores.ControladorCaixa import ControladorCaixa
from limites.TelaPopup import TelaPopup

class ControladorSistema:

    IMOVEIS = "IMOVEIS"
    PLATAFORMAS = "PLATAFORMAS"
    C_IMOVEIS = "C_IMOVEIS"
    R_IMOVEIS = "R_IMOVEIS"
    U_IMOVEIS = "U_IMOVEIS"
    D_IMOVEIS = "D_IMOVEIS"
    C_PLATAFORMAS = "C_PLATAFORMAS"
    R_PLATAFORMAS = "R_PLATAFORMAS"
    U_PLATAFORMAS = "U_PLATAFORMAS"
    D_PLATAFORMAS = "D_PLATAFORMAS"
    U_SENHA = "U_SENHA"
    PROSSEGUIR = "PROSSEGUIR"
    SAIR = "SAIR"
    def __init__(self):
        self.__autenticado = False
        self.__ControladorReceitas= ControladorReceitas()
        self.__ControladorMenu= ControladorMenu()
        self.__ControladorSenha= ControladorSenha()
        self.__ControladorDespesas= ControladorDespesas()
        self.__ControladorSaques= ControladorSaques()
        self.__ControladorAportes= ControladorAportes()
        self.__ControladorRelatorios= ControladorRelatorios()
        self.__ControladorPlataformas= ControladorPlataformas()
        self.__ControladorImoveis= ControladorImoveis()
        self.__ControladorCaixa= ControladorCaixa()
        self.__tela = TelaPopup()

    def inicializar(self):
        while not self.autenticado:
            self.autenticado = self.__ControladorSenha.verificar_senha()

        while self.autenticado:
            match self.__ControladorMenu.abrir_menu():
                case self.PROSSEGUIR, self.U_SENHA:
                    self.__ControladorSenha.alterar_senha()
                case self.PROSSEGUIR, self.IMOVEIS:
                    self.__tela.mostra_popup("Aqui vai aparecer o menu de imóveis")
                    match self.__ControladorImoveis.abrir_menu():
                        case self.C_IMOVEIS:
                            self.__ControladorImoveis.cadastrar_imovel()
                        case self.R_IMOVEIS:
                            self.__ControladorImoveis.listar_imoveis()
                        case self.U_IMOVEIS:
                            self.__ControladorImoveis.alterar_imovel()
                        case self.D_IMOVEIS:
                            self.__ControladorImoveis.excluir_imovel()
                case self.PROSSEGUIR, self .PLATAFORMAS:
                    self.__tela.mostra_popup("Aqui vai aparecer o menu de plataformas")
                    match self.__ControladorPlataformas.abrir_menu():
                        case self.C_PLATAFORMAS:
                            self.__ControladorPlataformas.cadastrar_plataforma()
                        case self.R_PLATAFORMAS:
                            self.__ControladorPlataformas.listar_plataformas()
                        case self.U_PLATAFORMAS:
                            self.__ControladorPlataformas.alterar_plataforma()
                        case self.D_PLATAFORMAS:
                            self.__ControladorPlataformas.excluir_plataforma()
                case self.SAIR, None:
                    self.autenticado = False




    @property
    def autenticado(self):
        return self.__autenticado

    @autenticado.setter
    def autenticado(self, autenticado):
        self.__autenticado = autenticado

    def processar_operacao(self):
        pass