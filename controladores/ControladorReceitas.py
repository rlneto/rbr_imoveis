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


class ControladorReceitas:
    C_RECEITAS = "C_RECEITAS"
    R_RECEITAS = "R_RECEITAS"
    D_RECEITAS = "D_RECEITAS"
    PROXIMO = "PROXIMO"
    VOLTAR = "VOLTAR"

    def __init__(self):
        self.__dao = DAOReceita("receitas.pkl")
        self.__tela = TelaReceitas()

    def abrir_menu(self, ControladorImoveis, ControladorPlataformas):
        while True:
            match self.__tela.abrir_menu():
                case self.C_RECEITAS:
                    self.cadastrar_receita(ControladorImoveis, ControladorPlataformas)
                case self.R_RECEITAS:
                    self.listar_receitas()
                case self.D_RECEITAS:
                    self.excluir_receita(ControladorImoveis, ControladorPlataformas)
                case self.VOLTAR:
                    return
                case None:
                    return

    def cadastrar_receita(self, ControladorImoveis, ControladorPlataformas):
        imoveis = ControladorImoveis.pegar_todos_imoveis()
        plataformas = ControladorPlataformas.pegar_todas_plataformas()
        if not self.validar_existencia_imoveis(imoveis):
            return
        elif not self.validar_existencia_plataformas(plataformas):
            return

        valor, id_imovel, id_plataforma, obs, data, tags = self.__tela.cadastrar_receita(imoveis, plataformas)

        if valor is None and id_imovel is None and id_plataforma is None and obs is None and data is None and tags is None:
            return

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

        imovel = ControladorImoveis.find_imovel_por_id(id_imovel)
        if imovel is None:
            self.__tela.mostra_popup("Imóvel não encontrado.")
            return

        plataforma = ControladorPlataformas.find_plataforma_por_id(id_plataforma)
        if plataforma is None:
            self.__tela.mostra_popup("Plataforma não encontrada.")

        id = ControladorGeraIdReceita().gera_id()
        if self.__dao.create(id, obs=obs, valor=valor, data=data, imovel=imovel, plataforma=plataforma, tags=tags):
            self.__tela.mostra_popup("Receita cadastrada com sucesso.")
        else:
            self.__tela.mostra_popup("Erro ao cadastrar receita.")

    def excluir_receita(self, ControladorImoveis, ControladorPlataformas):
        id_receita = self.__tela.excluir_receita(self.__dao.read())
        if id_receita is None:
            return

        if not self.validar_id(id_receita):
            return

        if self.__dao.delete(id_receita):
            self.__tela.mostra_popup("Receita excluída com sucesso.")
        else:
            self.__tela.mostra_popup("Erro ao excluir receita.")

    def listar_receitas(self):
        self.__tela.exibir_receitas(self.__dao.read())

    def find_receita(self, id):
        return [receita for receita in self.__dao.read() if receita.id == id][0]

    def validar_campos_vazios(self, valor, obs, data, id_imovel, id_plataforma, tags):
        if (valor is None or
                obs is None or
                data is None or
                id_imovel is None or
                id_plataforma is None or
                tags is None):
            self.__tela.mostra_popup("Preencha todos os campos.")
            return True
        return False

    def validar_valor(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            self.__tela.mostra_popup("Valor inválido. Deve ser um número.")
            return False
        return True

    def validar_id(self, id):
        if id.strip() == "":
            self.__tela.mostra_popup("ID não pode estar em branco.")
            return False
        if not id.isdigit():
            self.__tela.mostra_popup("ID inválido. Deve ser um número inteiro.")
            return False
        return True

    def validar_existencia_plataforma(self, id_plataforma, plataformas):
        if not any(plataforma.id == id_plataforma for plataforma in plataformas):
            self.__tela.mostra_popup("Plataforma não encontrada.")
            return False
        return True

    def validar_existencia_imovel(self, id_imovel, imoveis):
        if not any(imovel.id == id_imovel for imovel in imoveis):
            self.__tela.mostra_popup("Imóvel não encontrado.")
            return False
        return True

    def validar_existencia_imoveis(self, imoveis):
        if imoveis == []:
            self.__tela.mostra_popup("Não há imóveis cadastrados.")
            return False
        return True

    def validar_existencia_plataformas(self, plataformas):
        if plataformas == []:
            self.__tela.mostra_popup("Não há plataformas cadastradas.")
            return False
        return True

    def validar_tags(self, tags):
        if len(tags) == 0:
            self.__tela.mostra_popup("Adicione ao menos uma tag.")
            return False
        return True