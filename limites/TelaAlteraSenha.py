#######################################################
# 
# TelaAlteraSenha.py
# Python implementation of the Class TelaAlteraSenha
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela
import PySimpleGUI as sg


class TelaAlteraSenha(Tela):

    def __init__(self):
        super().__init__()
        self.__window = None

    def altera_senha(self):
        sg.theme('Reddit')
        column1 = [[sg.Text('Chave de acesso:', font=("Helvetica", 15), ), sg.Input(key='senha', password_char='*', )]]
        layout = [
            [sg.Column([[sg.Text('Alterar chave de acesso!', font=("Helvetica", 20))]],
                        pad=(30, 20))],
            [sg.Column(column1, pad=(30, 30))],
            [sg.Button('Confirmar', pad=(30, 30))]
        ]

        self.__window = sg.Window('RBR Imóveis').Layout(layout)
        button, values = self.__window.Read()
        if button is None:
            self.__window.Close()
            return None
        self.__window.Close()
        return values['senha']

