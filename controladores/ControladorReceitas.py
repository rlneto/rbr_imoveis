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
    PROXIMO = "PROXIMO"
    VOLTAR = "VOLTAR"

    def __init__(self):
        self.__dao = DAOReceita("receitas.pkl")
        self.__tela = TelaReceitas()
        self.__controlador_gera_id = ControladorGeraIdReceita()

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

        valor, id_imovel, id_plataforma, obs, data, tags = self.__tela.cadastrar_receita(imoveis, plataformas)

        if self.validar_campos_vazios(valor, obs, data, id_imovel, id_plataforma, tags):
            return

        if not self.validar_valor(valor):
            return

        if not self.validar_existencia_imovel(id_imovel, imoveis):
            return

        if not self.validar_existencia_plataforma(id_plataforma, plataformas):
            return

        if not self.validar_tags(tags):
            return

        imovel = controlador_imoveis.find_imovel_por_id(id_imovel)
        if imovel is None:
            self.__tela.mostra_popup("Imóvel não encontrado.")
            return

        plataforma = controlador_plataformas.find_plataforma_por_id(id_plataforma)
        if plataforma is None:
            self.__tela.mostra_popup("Plataforma não encontrada.")

        id_receita = self.__controlador_gera_id.gera_id()
        if self.__dao.create(id_receita, obs=obs, valor=valor, data=data, imovel=imovel,
                             plataforma=plataforma, tags=tags):
            self.__tela.mostra_popup("Receita cadastrada com sucesso.")
        else:
            self.__tela.mostra_popup("Erro ao cadastrar receita.")

    def excluir_receita(self):
        id_receita = self.__tela.excluir_receita(self.__dao.read())
        if id_receita is None:
            self.tela.mostra_popup("Nenhuma receita selecionada.")

        if self.__dao.delete(int(id_receita)):
            self.__tela.mostra_popup("Receita excluída com sucesso.")
        else:
            self.__tela.mostra_popup("Erro ao excluir receita.")

    def find_receita(self, id_receita: int) -> Receita:
        return [receita for receita in self.__dao.read() if receita.id == id_receita][0]

    def validar_campos_vazios(self, valor: float, obs: str, data: str,
                              id_imovel: int, id_plataforma: int, tags: list[str]) -> bool:
        if (valor is None or
                obs is None or
                data is None or
                id_imovel is None or
                id_plataforma is None or
                tags is None):
            self.__tela.mostra_popup("Preencha todos os campos.")
            return True
        return False

    def validar_valor(self, valor: float) -> bool:
        try:
            float(valor)
        except ValueError:
            self.__tela.mostra_popup("Valor inválido. Deve ser um número.")
            return False
        return True

    def validar_existencia_plataforma(self, id_plataforma: int, plataformas: list[Plataforma]) -> bool:
        if not any(plataforma.id == id_plataforma for plataforma in plataformas):
            self.__tela.mostra_popup("Plataforma não encontrada.")
            return False
        return True

    def validar_existencia_imovel(self, id_imovel: int, imoveis: list[Imovel]) -> bool:
        if not any(imovel.id == id_imovel for imovel in imoveis):
            self.__tela.mostra_popup("Imóvel não encontrado.")
            return False
        return True

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

    def validar_tags(self, tags: list[str]) -> bool:
        if len(tags) == 0:
            self.__tela.mostra_popup("Adicione ao menos uma tag.")
            return False
        return True

    def listar_receitas(self):
        self.__tela.exibir_receitas(self.__dao.read())
