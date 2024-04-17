#######################################################
# 
# TelaImoveis.py
# Python implementation of the Class TelaImoveis
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela
import PySimpleGUI as sg
class TelaImoveis(Tela):

    C_IMOVEIS = "C_IMOVEIS"
    R_IMOVEIS = "R_IMOVEIS"
    U_IMOVEIS = "U_IMOVEIS"
    D_IMOVEIS = "D_IMOVEIS"
    PROSSEGUIR = "PROSSEGUIR"
    VOLTAR = "VOLTAR"
    def __init__(self):
        self.__window = None

    def abrir_menu(self):
        sg.theme('Reddit')
        column1 = [[sg.Radio('Cadastrar imóveis', group_id='Imoveis',font=("Helvetica", 15), key=self.C_IMOVEIS)],
                     [sg.Radio('Exibir imóveis', group_id='Imoveis',font=("Helvetica", 15), key=self.R_IMOVEIS)],
                     [sg.Radio('Alterar imóveis', group_id='Imoveis',font=("Helvetica", 15), key=self.U_IMOVEIS)],
                     [sg.Radio('Excluir imóveis', group_id='Imoveis',font=("Helvetica", 15), key=self.D_IMOVEIS)]]

        layout = [[sg.Text('Sobre Imóveis', font=("Helvetica", 20), pad=((50,200),(30,30)))],
                    [sg.Column(column1, pad=(30, 30))],
                    [[sg.Button(button_text=('Voltar'), key=self.VOLTAR, pad=(20, 20), button_color=('white', 'red')), sg.Button('Confirmar', pad=(0, 20), key='PROSSEGUIR')]]
                  ]
        self.__window = sg.Window('RBR Imóveis').Layout(layout)
        button, values = self.__window.Read()
        if button == 'VOLTAR' or button is None:
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
