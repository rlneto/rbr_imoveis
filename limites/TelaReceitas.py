#######################################################
# 
# TelaReceitas.py
# Python implementation of the Class TelaReceitas
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela
import PySimpleGUI as sg

class TelaReceitas(Tela):

    C_RECEITA = "C_RECEITA"
    R_RECEITA = "R_RECEITA"
    D_RECEITA = "D_RECEITA"

    def __init__(self, imoveis: list, plataformas: list):
        super().__init__()
        self.__imoveis = imoveis
        self.__plataformas = plataformas
        self.__window = None

    def abrir_menu(self):
        layout = [
            [sg.Button("Cadastrar Receita", key=self.C_RECEITA)],
            [sg.Button("Listar Receitas", key=self.R_RECEITA)],
            [sg.Button("Excluir Receita", key=self.D_RECEITA)],
            [sg.Button("Voltar", key=self.VOLTAR)]
        ]
        self.__window = sg.Window("Menu Receitas").Layout(layout)
        return self.__window.Read()

    def cadastrar_receita(self, imoveis: list, plataformas: list):
        layout = [
            [sg.Text("Cadastrar Receita")],
            [sg.Text("Imovel"), sg.InputCombo(imoveis, key="imovel")],
            [sg.Text("Plataforma"), sg.InputCombo(plataformas, key="plataforma")],
            [sg.Text("Valor"), sg.InputText(key="valor")],
            [sg.Text("Data"), sg.InputText(key="data")],
            sg.Text("Tags"), sg.InputText(key="tags"),
            [sg.Button("Cadastrar", key="Cadastrar")],
            [sg.Button("Voltar", key="Voltar")]
        ]
        self.__window = sg.Window("Cadastrar Receita").Layout(layout)
        return self.__window.Read()

    def listar_receitas(self, receitas: list):
        layout = [
            [sg.Text("Listar Receitas")],
            [sg.Listbox(receitas, key="receitas")],
            [sg.Button("Voltar", key="Voltar")]
        ]
        self.__window = sg.Window("Listar Receitas").Layout(layout)
        return self.__window.Read()

    def excluir_receita(self, receitas: list):
        layout = [
            [sg.Text("Excluir Receita")],
            [sg.Listbox(receitas, key="receitas")],
            [sg.Button("Excluir", key="Excluir")],
            [sg.Button("Voltar", key="Voltar")]
        ]
        self.__window = sg.Window("Excluir Receita").Layout(layout)
        return self.__window.Read()

    def cadastrar_erro(self):
        self.mostra_popup("Erro ao cadastrar receita")

    def listar_erro(self):
        self.mostra_popup("Erro ao listar receitas")

    def excluir_erro(self):
        self.mostra_popup("Erro ao excluir receita")

    def cadastrar_sucesso(self):
        self.mostra_popup("Receita cadastrada com sucesso")

    def excluir_sucesso(self):
        self.mostra_popup("Receita excluída com sucesso")
