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

class ControladorSistema:

    IMOVEIS = "IMOVEIS"
    PLATAFORMAS = "PLATAFORMAS"
    DESPESAS = "DESPESAS"
    C_IMOVEIS = "C_IMOVEIS"
    R_IMOVEIS = "R_IMOVEIS"
    U_IMOVEIS = "U_IMOVEIS"
    D_IMOVEIS = "D_IMOVEIS"
    C_PLATAFORMAS = "C_PLATAFORMAS"
    R_PLATAFORMAS = "R_PLATAFORMAS"
    U_PLATAFORMAS = "U_PLATAFORMAS"
    D_PLATAFORMAS = "D_PLATAFORMAS"
    C_DESPESAS = "C_DESPESAS"
    R_DESPESAS = "R_DESPESAS"
    D_DESPESAS = "D_DESPESAS"
    C_RECEITAS = "C_RECEITAS"
    R_RECEITAS = "R_RECEITAS"
    D_RECEITAS = "D_RECEITAS"
    CAIXA = "CAIXA"
    U_SENHA = "U_SENHA"
    PROSSEGUIR = "PROSSEGUIR"
    SAIR = "SAIR"
    def __init__(self):
        self.__autenticado = False
        # self.__autenticado = True # Para testes
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

    def inicializar(self):
        while not self.autenticado:
            self.autenticado = self.__ControladorSenha.verificar_senha()
            if not self.autenticado:
                self.__ControladorSenha.erro_senha()

        while True:
            match self.__ControladorMenu.abrir_menu():
                case self.PROSSEGUIR, self.U_SENHA:
                    self.__ControladorSenha.alterar_senha()
                case self.IMOVEIS:
                    match self.__ControladorImoveis.abrir_menu():
                        case self.C_IMOVEIS:
                            self.__ControladorImoveis.cadastrar_imovel()
                        case self.R_IMOVEIS:
                            self.__ControladorImoveis.listar_imoveis()
                        case self.U_IMOVEIS:
                            self.__ControladorImoveis.alterar_imovel()
                        case self.D_IMOVEIS:
                            self.__ControladorImoveis.excluir_imovel()
                case self.PLATAFORMAS:
                    match self.__ControladorPlataformas.abrir_menu():
                        case self.C_PLATAFORMAS:
                            self.__ControladorPlataformas.cadastrar_plataforma()
                        case self.R_PLATAFORMAS:
                            self.__ControladorPlataformas.listar_plataformas()
                        case self.U_PLATAFORMAS:
                            self.__ControladorPlataformas.alterar_plataforma()
                        case self.D_PLATAFORMAS:
                            self.__ControladorPlataformas.excluir_plataforma()
                case self.DESPESAS:
                    match self.__ControladorDespesas.abrir_menu(self.__ControladorImoveis):
                        case self.C_DESPESAS:
                            self.__ControladorDespesas.cadastrar_despesa(self.__ControladorImoveis)
                        case self.R_DESPESAS:
                            self.__ControladorDespesas.listar_despesas()
                        case self.D_DESPESAS:
                            self.__ControladorDespesas.excluir_despesa()
                case self.RECEITAS:
                    match self.__ControladorReceitas.abrir_menu(self.__ControladorImoveis, self.__ControladorPlataformas):
                        case self.C_RECEITAS:
                            self.__ControladorReceitas.cadastrar_receita(self.__ControladorImoveis, self.__ControladorPlataformas)
                        case self.R_RECEITAS:
                            self.__ControladorReceitas.listar_receitas(self.__ControladorImoveis, self.__ControladorPlataformas)
                        case self.D_RECEITAS:
                            self.__ControladorReceitas.excluir_receita()

                case self.CAIXA:
                    self.__ControladorCaixa.exibir_caixa()
                case self.U_SENHA:
                    self.__ControladorSenha.alterar_senha()
                case self.SAIR:
                    exit()




    @property
    def autenticado(self):
        return self.__autenticado

    @autenticado.setter
    def autenticado(self, autenticado):
        self.__autenticado = autenticado

    def processar_operacao(self):
        pass