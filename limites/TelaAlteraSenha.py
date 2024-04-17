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
        self.__window = None

    def altera_senha(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Nova Senha:'), sg.Input(key='senha', password_char='*')],
            [sg.Button('Alterar')]
        ]
        self.__window = sg.Window('Alterar Senha', disable_close=True).Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return values['senha']
