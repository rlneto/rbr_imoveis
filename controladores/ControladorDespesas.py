#######################################################
# 
# ControladorDespesas.py
# Python implementation of the Class ControladorDespesas
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
import datetime
from limites.TelaDespesas import TelaDespesas
from DAOs.DAODespesa import DAODespesa
from controladores.ControladorGeraIdDespesa import ControladorGeraIdDespesa


class ControladorDespesas:
    C_DESPESAS = "C_DESPESAS"
    R_DESPESAS = "R_DESPESAS"
    D_DESPESAS = "D_DESPESAS"
    PROXIMO = "PROXIMO"
    VOLTAR = "VOLTAR"

    def __init__(self):
        self.__dao = DAODespesa("despesas.pkl")
        self.__tela = TelaDespesas()

    def abrir_menu(self, controladorimoveis):
        while True:
            match self.__tela.abrir_menu():
                case self.C_DESPESAS:
                    self.cadastrar_despesa(controladorimoveis)
                case self.R_DESPESAS:
                    self.listar_despesas()
                case self.D_DESPESAS:
                    self.excluir_despesa()
                case self.VOLTAR:
                    return
                case None:
                    return

    def cadastrar_despesa(self, controlador_imovel):
        imoveis = controlador_imovel.pegar_todos_imoveis()
        if not self.validar_existencia_imoveis(imoveis):
            return

        valor, id_imovel, obs, data, tags = self.__tela.cadastrar_despesa(imoveis)

        if valor is None and id_imovel is None and obs is None and data is None and tags is None:
            return

        if self.validar_campos_vazios(valor, obs, data, id_imovel, tags):
            return

        if not self.validar_valor(valor):
            return

        if not self.validar_existencia_imovel(id_imovel, imoveis):
            return

        imovel = controlador_imovel.find_imovel_por_id(id_imovel)

        id = ControladorGeraIdDespesa().gera_id()
        self.__dao.create(id, obs=obs, valor=valor, data=data, imovel=imovel, tags=tags)

    def excluir_despesa(self):
        despesas = self.__dao.read()
        if not despesas:
            self.__tela.mostra_popup("Não há despesas cadastradas!")
        else:
            id_despesa = self.__tela.excluir_despesa(despesas)
            if id_despesa is None:
                return

            if not self.validar_id(id_despesa):
                return

            self.__dao.delete(int(id_despesa))

    def listar_despesas(self):
        despesas = self.__dao.read()
        if not despesas:
            self.__tela.mostra_popup("Não há despesas cadastradas!")
        else:
            self.__tela.exibir_despesas(despesas)

    def find_despesa(self, id):
        return [despesa for despesa in self.__dao.read() if despesa.id == id][0]

    # Validações cadastrar Despesa
    def validar_campos_vazios(self, valor, obs, data, id_imovel, tags):
        if (data.strip() == "" or
                valor.strip() == "" or
                obs.strip() == "" or
                len(tags) == 0):
            self.__tela.mostra_popup("Todos os campos devem ser preenchidos.")
            return True
        return False

    def validar_existencia_imoveis(self, imoveis):
        if not imoveis:
            self.__tela.mostra_popup("Você deve possuir imóveis cadastrados para prosseguir!")
            return False
        return True

    def validar_valor(self, valor):
        try:
            valor = float(valor)
            if valor <= 0:
                self.__tela.mostra_popup("O valor da despesa deve ser um número maior que zero.")
                return False
            return True
        except ValueError:
            self.__tela.mostra_popup("O valor da despesa deve ser um número.")
            return False

    def validar_existencia_imovel(self, id_imovel, imoveis):
        if id_imovel not in [imovel.id for imovel in imoveis]:
            self.__tela.mostra_popup("Imóvel selecionado não encontrado.")
            return False
        return True


    # Validação excluir Despesa
    def validar_id(self, id_despesa):
        if not id_despesa.strip():
            self.__tela.mostra_popup("O campo ID não pode estar vazio.")
            return False

        if not id_despesa.isdigit():
            self.__tela.mostra_popup("O ID da despesa deve ser um número inteiro.")
            return False

        id_despesa = int(id_despesa)

        if not any(despesa.id == id_despesa for despesa in self.__dao.read()):
            self.__tela.mostra_popup(f"Despesa com ID {id_despesa} não encontrada.")
            return False

        return True

    # Utilizar para os relatórios depois
    def listar_despesas_ano(self, ano):
        despesas = self.__dao.read()
        despesas_ano = [despesa for despesa in despesas if
                        datetime.datetime.strptime(despesa.data, '%d/%m/%Y').year == ano]
        if despesas_ano:
            print(f"Despesas do ano {ano}:")
            for despesa in despesas_ano:
                print(
                    f"ID: {despesa.id} - Valor: {despesa.valor} - Data: {despesa.data} - Imóvel: {despesa.imovel.titulo}")
        else:
            print(f"Não há despesas registradas para o ano {ano}.")

    def listar_despesas_imovel(self, id_imovel):
        despesas_imovel = [despesa for despesa in self.__dao.read() if despesa.imovel.id == id_imovel]
        if despesas_imovel:
            print(f"Despesas do imóvel ID {id_imovel}:")
            for despesa in despesas_imovel:
                print(f"ID: {despesa.id} - Valor: {despesa.valor} - Data: {despesa.data}")
        else:
            print(f"Não há despesas registradas para o imóvel ID {id_imovel}.")
