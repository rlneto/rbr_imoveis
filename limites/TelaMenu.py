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
    IMOVEIS = "IMOVEIS"
    PLATAFORMAS = "PLATAFORMAS"
    U_SENHA = "U_SENHA"
    PROSSEGUIR = "PROSSEGUIR"
    SAIR = "SAIR"
    def __init__(self):
        self.__window = None

    def abrir_menu(self):
        sg.theme('TealMono')
        layout = [
            [sg.Text('Menu')],
            [sg.Radio('Imóveis', group_id='menu', key='IMOVEIS')],
            [sg.Radio('Plataformas', group_id='menu', key='PLATAFORMAS')],
            [sg.Radio('Alterar Senha', group_id='menu', key='U_SENHA')],
            [sg.Button('Prosseguir', key='PROSSEGUIR')],
            [sg.Button('Sair', key='SAIR')]
        ]
        self.__window = sg.Window('Menu Principal').Layout(layout)
        button, values = self.__window.Read()
        if button == 'SAIR':
            self.__window.Close()
            return None
        else:
            for key in values:
                if values[key]:
                    escolha = key
                    self.__window.Close()
                    return escolha
            self.__window.Close()
            return None



