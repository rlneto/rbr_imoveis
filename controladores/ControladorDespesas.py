#######################################################
# 
# ControladorDespesas.py
# Python implementation of the Class ControladorDespesas
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from limites.TelaDespesas import TelaDespesas
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

    def abrir_menu(self):
        while True:
            match self.__tela.abrir_menu():
                case self.C_DESPESAS:
                    self.cadastrar_despesa()
                case self.R_DESPESAS:
                    self.listar_despesas()
                case self.D_DESPESAS:
                    self.excluir_despesa()
                case self.VOLTAR:
                    return
                case None:
                    return


    def cadastrar_despesa(self):
        # self.__controlador_sistema.controlador_imovel.lista_imoveis()
        valor, obs, data, id_imovel, tags = self.__tela.cadastrar_despesa()
        # imovel = self.__controlador_sistema.controlador_imovel.pega_imovel_por_id(int(id_imovel))
        if valor is None or obs is None or data is None or id_imovel is None or tags is None:
            return
        else:
            self.__dao.create(id=ControladorGeraIdDespesa().gera_id(), obs= obs, valor= valor, data= data, imovel= imovel, tags= tags)

    def excluir_despesa(self):
        id_despesa = self.__tela.excluir_despesa(self.__dao.read())
        if id_despesa is None:
            return
        else:
            self.__dao.delete(int(id_despesa))

    def listar_despesas(self):
        self.__tela.exibir_despesas(self.__dao.read())

    def exibir_despesa(self):
        pass

    def find_despesa(self, id):
        return [despesa for despesa in self.__dao.read() if despesa.id == id][0]

    def listar_despesas_ano(self):
        pass

    def listar_despesas_imovel(self):
        pass