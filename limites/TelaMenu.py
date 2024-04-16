#######################################################
# 
# TelaMenu.py
# Python implementation of the Class TelaMenu
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela
import PySimpleGUI as sg

class TelaMenu(Tela):
    def __init__(self):
        self.__window = None

    def abrir_menu(self):
        sg.theme('TealMono')
        layout = [
            [sg.Text('Menu')],
            [sg.Button('Cadastrar Imóveis', key='C_IMOVEIS')],
            [sg.Button('Consultar Imóveis', key='R_IMOVEIS')],
            [sg.Button('Alterar Imóveis', key='U_IMOVEIS')],
            [sg.Button('Excluir Imóveis', key='D_IMOVEIS')],
            [sg.Button('Cadastrar Plataformas', key='C_PLATAFORMAS')],
            [sg.Button('Consultar Plataformas', key='R_PLATAFORMAS')],
            [sg.Button('Alterar Plataformas', key='U_PLATAFORMAS')],
            [sg.Button('Excluir Plataformas', key='D_PLATAFORMAS')],
            [sg.Button('Alterar Senha', key='U_SENHA')],
            [sg.Button('Sair', key='SAIR')]
        ]
        self.__window = sg.Window('Menu').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        print(button, values)
        return button




