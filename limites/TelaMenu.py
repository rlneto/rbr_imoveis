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
        super().__init__()
        self.__window = None

    def abrir_menu(self):
        sg.theme('Reddit')
        column1 = [[sg.Radio('Imóveis', font=('Helvetica', 15), group_id='menu', key='IMOVEIS')],
                   [sg.Radio('Receitas', font=('Helvetica', 15), group_id='menu', key='RECEITAS', disabled=False)],
                   [sg.Radio('Despesas', font=('Helvetica', 15), group_id='menu', key='DESPESAS')],
                   [sg.Radio('Relatórios', font=('Helvetica', 15), group_id='menu', key='RELATORIOS')]]
        column2 = [[sg.Radio('Aportes', font=('Helvetica', 15), group_id='menu', key='APORTES', disabled=True)],
                   [sg.Radio('Saques', font=('Helvetica', 15), group_id='menu', key='SAQUES')],
                   [sg.Radio('Plataformas', font=('Helvetica', 15), group_id='menu', key='PLATAFORMAS')],
                   [sg.Radio('Caixa', font=('Helvetica', 15), group_id='menu', key='CAIXA', disabled=False)],
                   [sg.Radio('Alterar chave de acesso', font=('Helvetica', 15), group_id='menu', key='U_SENHA')]]
        layout = [
            [sg.Text('Sistema de Gerenciamento de Imóveis', justification='center', font=("Helvetica", 20),
                     pad=(20, 20))],
            [sg.Column(column1, pad=(30, 30)), sg.Column(column2, pad=(30, 30))],
            # [sg.Text('Caixa = 0 R$', font=('Helvetica', 15), pad=(40, 15))],
            [[sg.Button(button_text=('Sair'), key='SAIR', pad=(20, 20), button_color=('white', 'red')),
              sg.Button('Confirmar', pad=(0, 20), key='PROSSEGUIR')]]
        ]
        self.__window = sg.Window('RBR Imóveis', layout)
        button, values = self.__window.Read()
        if button is None or button == 'SAIR':
            exit()
        else:
            for key in values:
                if values[key]:
                    escolha = key
                    self.__window.Close()
                    return escolha
            self.__window.Close()
            return None
