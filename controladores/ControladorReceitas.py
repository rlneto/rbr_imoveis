#######################################################
# 
# ControladorReceitas.py
# Python implementation of the Class ControladorReceitas
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from limites.TelaReceitas import TelaReceitas
from DAOs.DAOReceita import DAOReceita
from controladores.ControladorGeraIdReceita import ControladorGeraIdReceita
from controladores.ControladorImoveis import ControladorImoveis
from controladores.ControladorPlataformas import ControladorPlataformas
from entidades.Imovel import Imovel
from entidades.Plataforma import Plataforma
from entidades.Receita import Receita


class ControladorReceitas:
    C_RECEITAS = "C_RECEITAS"
    R_RECEITAS = "R_RECEITAS"
    D_RECEITAS = "D_RECEITAS"
    EXCLUIR = "Excluir"
    PROSSEGUIR = "PROSSEGUIR"
    PROXIMO = "PROXIMO"
    VOLTAR = "VOLTAR"

    def __init__(self):
        self.__dao = DAOReceita("receitas.pkl")
        self.__tela = TelaReceitas()
        self.__controlador_gera_id = ControladorGeraIdReceita()

    @property
    def dao(self):
        return self.__dao

    def abrir_menu(self, controlador_imoveis: ControladorImoveis, controlador_plataformas: ControladorPlataformas):
        while True:
            match self.__tela.abrir_menu():
                case self.C_RECEITAS:
                    self.cadastrar_receita(controlador_imoveis, controlador_plataformas)
                case self.R_RECEITAS:
                    self.listar_receitas()
                case self.D_RECEITAS:
                    self.excluir_receita()
                case self.VOLTAR:
                    return
                case None:
                    return

    def cadastrar_receita(self, controlador_imoveis: ControladorImoveis,
                          controlador_plataformas: ControladorPlataformas):
        imoveis = controlador_imoveis.pegar_todos_imoveis()
        plataformas = controlador_plataformas.pegar_todas_plataformas()
        if not self.validar_existencia_imoveis(imoveis):
            return
        elif not self.validar_existencia_plataformas(plataformas):
            return

        valor, id_imovel, id_plataforma, obs, data, tags, action = self.__tela.cadastrar_receita(imoveis, plataformas)

        if not self.validar_campos_vazios(valor, id_imovel, id_plataforma, obs, data, tags):
            if action == self.PROSSEGUIR:
                self.__tela.mostra_popup("Preencha todos os campos.")
            return


        if not valor.isdigit():
            self.__tela.mostra_popup("Valor inválido. Deve ser um número.")
            return

        imovel = [imovel for imovel in imoveis if imovel.id == id_imovel][0]
        plataforma = [plataforma for plataforma in plataformas if plataforma.id == id_plataforma][0]

        id_receita = self.__controlador_gera_id.gera_id()
        if self.__dao.create(id_receita, obs=obs, valor=valor, data=data, imovel=imovel,
                             plataforma=plataforma, tags=tags):
            self.__tela.mostra_popup("Receita cadastrada com sucesso.")
            return
        else:
            self.__tela.mostra_popup("Erro ao cadastrar receita.")
            return

    def excluir_receita(self):
        leitura = self.__dao.read()
        id_receita, action = self.__tela.excluir_receita(leitura)
        if id_receita is None:
            return
        elif action == self.EXCLUIR:
            success = self.__dao.delete(id_receita)
            if success:
                self.__tela.mostra_popup("Receita excluída com sucesso.")
                return
            else:
                self.__tela.mostra_popup("Erro ao excluir receita.")
                return
        else:
            self.__tela.mostra_popup("Erro ao excluir receita.")
            return

    def find_receita(self, id_receita: int) -> Receita:
        return [receita for receita in self.__dao.read() if receita.id == id_receita][0]


    def validar_existencia_imoveis(self, imoveis: list[Imovel]) -> bool:
        if not imoveis:
            self.__tela.mostra_popup("Não há imóveis cadastrados.")
            return False
        return True

    def validar_existencia_plataformas(self, plataformas: list[Plataforma]) -> bool:
        if not plataformas:
            self.__tela.mostra_popup("Não há plataformas cadastradas.")
            return False
        return True

    def listar_receitas(self):
        leitura = self.__dao.read()
        self.__tela.exibir_receitas(leitura)
        return
    
    def pegar_receitas_por_imovel(self, id_imovel):
        receitas = self.__dao.read() 
        receitas_imovel = [receita for receita in receitas if receita.imovel.id == id_imovel]
        return receitas_imovel

    def validar_campos_vazios(self, valor: float, id_imovel: int, id_plataforma: int, obs: str, data: str, tags: str) -> bool:
        if not (valor and id_imovel and id_plataforma and obs and data and tags):
            return False
        return True