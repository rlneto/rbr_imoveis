#######################################################
# 
# TelaExibeImoveis.py
# Python implementation of the Class TelaExibeImoveis
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela
import PySimpleGUI as sg

class TelaExibeImoveis(Tela):

        def __init__(self):
            self.__window = None

        def exibir_imoveis(self, imoveis):
            sg.theme('TealMono')
            layout = [
                [sg.Text('Imóveis')],
                [sg.Listbox(values=imoveis, size=(100,6))],
                [sg.Button('Voltar')]
            ]
            self.__window = sg.Window('Imóveis').Layout(layout)
            button, values = self.__window.Read()
            self.close()
            return button

        def close(self):
            self.__window.Close()
            self.__window = None