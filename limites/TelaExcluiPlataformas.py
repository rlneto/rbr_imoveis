#######################################################
# 
# TelaExcluiPlataformas.py
# Python implementation of the Class TelaExcluiPlataformas
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela
import PySimpleGUI as sg

class TelaExcluiPlataformas(Tela):
    def __init__(self):
        self.__window = None

    def excluir_plataforma(self, plataformas):

        sg.theme('Reddit')
        layout = [
            [sg.Text('Excluir Plataforma')],
            [sg.Listbox(values=plataformas, size=(100,6))],
            [sg.Button('Excluir'), sg.Button('Cancelar')]
        ]
        self.__window = sg.Window('Excluir Plataforma').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        if button == 'Excluir':
            return values[0][0].id
        else:
            return None

    def close(self):
        self.__window.Close()
        self.__window = None