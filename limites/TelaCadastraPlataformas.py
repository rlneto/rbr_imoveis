#######################################################
# 
# TelaCadastraPlataformas.py
# Python implementation of the Class TelaCadastraPlataformas
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela
import PySimpleGUI as sg

class TelaCadastraPlataformas(Tela):

    def __init__(self):
        self.__window = None

    def cadastrar_plataforma(self):
        sg.theme('TealMono')
        layout = [
            [sg.Text('Cadastrar Plataforma')],
            [sg.Text('Titulo', size=(15, 1)), sg.InputText()],
            [sg.Text('Descrição', size=(15, 1)), sg.InputText()],
            [sg.Button('Cadastrar'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Cadastrar Plataforma').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        if button == 'Cadastrar':
            print(values)
            return values[0], values[1]
        else:
            return None

    def close(self):
        self.__window.Close()
        self.__window = None