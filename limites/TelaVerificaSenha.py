#######################################################
# 
# TelaVerificaSenha.py
# Python implementation of the Class TelaVerificaSenha
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela

import PySimpleGUI as sg

class TelaVerificaSenha(Tela):

    def __init__(self):
        self.__window = None

    def verifica_senha(self):
        sg.theme('TealMono')
        layout = [
            [sg.Text('Lembrete: A senha padrão é "abc123"')],
            [sg.Text('Senha:'), sg.Input(key='senha', password_char='*')],
            [sg.Button('Verificar')]
        ]
        self.__window = sg.Window('Verificar Senha').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return values['senha']
