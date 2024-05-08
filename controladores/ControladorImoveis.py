#######################################################
# 
# ControladorImoveis.py
# Python implementation of the Class ControladorImoveis
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from limites.TelaImoveis import TelaImoveis
from limites.TelaAlterarImoveis import TelaAlterarImoveis
from limites.TelaExcluiImoveis import TelaExcluiImoveis
from limites.TelaExibeImoveis import TelaExibeImoveis
from limites.TelaCadastraImoveis import TelaCadastraImoveis
from limites.TelaPopup import TelaPopup
from controladores.ControladorGeraIdImovel import ControladorGeraIdImovel
from DAOs.DAOImovel import DAOImovel

class ControladorImoveis:
    C_IMOVEIS = "C_IMOVEIS"
    R_IMOVEIS = "R_IMOVEIS"
    U_IMOVEIS = "U_IMOVEIS"
    D_IMOVEIS = "D_IMOVEIS"
    PROSSEGUIR = "PROSSEGUIR"
    VOLTAR = "VOLTAR"
    SAIR = "SAIR"

    def __init__(self):
        self.__dao = DAOImovel("./imoveis.pkl")
        self.__tela = TelaImoveis()
        self.__tela_alterar = TelaAlterarImoveis()
        self.__tela_excluir = TelaExcluiImoveis()
        self.__tela_exibir = TelaExibeImoveis()
        self.__tela_cadastrar = TelaCadastraImoveis()
        self.__tela_popup = TelaPopup()

    def abrir_menu(self):
        while True:
            match self.__tela.abrir_menu():
                case self.C_IMOVEIS:
                    self.cadastrar_imovel()
                case self.R_IMOVEIS:
                    self.listar_imoveis()
                case self.U_IMOVEIS:
                    self.alterar_imovel()
                case self.D_IMOVEIS:
                    self.excluir_imovel()
                # case self.PROSSEGUIR:
                #     return self.PROSSEGUIR
                case self.VOLTAR:
                    return
                case None:
                    return

    def alterar_imovel(self):
        novo_imovel = self.__tela_alterar.selecionar_imovel(self.__dao.read())
        if novo_imovel is None:
            return
        else:
            self.__dao.update(id=novo_imovel[2], novo_titulo=novo_imovel[0], nova_desc=novo_imovel[1])

    def cadastrar_imovel(self):
        titulo, desc = self.__tela_cadastrar.cadastrar_imovel()
        if titulo is None:
            return
        else:
            self.__dao.create(desc=desc, titulo=titulo, id=ControladorGeraIdImovel().gera_id())

    def excluir_imovel(self):
        id_imovel = self.__tela_excluir.excluir_imovel(self.__dao.read())
        if id_imovel is None:
            return
        else:
            self.__dao.delete(int(id_imovel))

    def exibir_imovel(self):
        pass

    def find_imovel(self, nome_imovel):
        return [imovel for imovel in self.__dao.read() if imovel.titulo == nome_imovel][0]


    def listar_imoveis(self):
        self.__tela_exibir.exibir_imoveis(self.__dao.read())

