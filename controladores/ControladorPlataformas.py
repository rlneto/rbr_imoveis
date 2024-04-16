#######################################################
# 
# ControladorPlataformas.py
# Python implementation of the Class ControladorPlataformas
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from limites.TelaPlataformas import TelaPlataformas
from limites.TelaAlterarPlataformas import TelaAlterarPlataformas
from limites.TelaExcluiPlataformas import TelaExcluiPlataformas
from limites.TelaExibePlataformas import TelaExibePlataformas
from limites.TelaCadastraPlataformas import TelaCadastraPlataformas
from controladores.ControladorGeraIdPlataforma import ControladorGeraIdPlataforma
from DAOs.DAOPlataforma import DAOPlataforma
from limites.TelaPopup import TelaPopup


class ControladorPlataformas:
    C_PLATAFORMAS = "C_PLATAFORMAS"
    R_PLATAFORMAS = "R_PLATAFORMAS"
    U_PLATAFORMAS = "U_PLATAFORMAS"
    D_PLATAFORMAS = "D_PLATAFORMAS"
    PROXIMO = "PROXIMO"
    VOLTAR = "VOLTAR"

    def __init__(self):
        self.__dao = DAOPlataforma("plataformas.pkl")
        self.__tela = TelaPlataformas()
        self.__tela_alterar = TelaAlterarPlataformas()
        self.__tela_excluir = TelaExcluiPlataformas()
        self.__tela_exibir = TelaExibePlataformas()
        self.__tela_cadastrar = TelaCadastraPlataformas()

    # def abrir_menu(self):
    #     while True:
    #         match self.__tela.abrir_menu():
    #             case PROXIMO, C_PLATAFORMAS:
    #                 self.cadastrar_plataforma()
    #             case PROXIMO, R_PLATAFORMAS:
    #                 self.listar_plataformas()
    #             case PROXIMO, U_PLATAFORMAS, nome_plataforma:
    #                 self.alterar_plataforma(nome_plataforma)
    #             case PROXIMO, D_PLATAFORMAS:
    #                 self.excluir_plataforma()
    #             case VOLTAR:
    #                 return

    def alterar_plataforma(self, id_plataforma):
        plataforma = [plataforma for plataforma in self.__dao.read() if plataforma.id == id_plataforma][0]
        nova_plataforma = self.__tela_alterar.alterar_plataforma(plataforma)
        self.__dao.update(id=id_plataforma, novo_titulo=nova_plataforma.titulo,
                          nova_desc=nova_plataforma.descricao)

    def cadastrar_plataforma(self):
        pass

    def excluir_plataforma(self):
        pass

    def exibir_plataforma(self):
        pass

    def find_plataforma(self, nome_plataforma):
        return [plataforma for plataforma in self.__dao.read() if plataforma.nome == nome_plataforma][0]

    def listar_plataformas(self):
        pass
