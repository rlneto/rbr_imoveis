#######################################################
# 
# TelaReceitas.py
# Python implementation of the Class TelaReceitas
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from limites.Tela import Tela
import PySimpleGUI as sg
from entidades.Receita import Receita
from entidades.Imovel import Imovel
from entidades.Plataforma import Plataforma

class TelaReceitas(Tela):
    def __init__(self):
        super().__init__()
        self.__window = None

    def abrir_menu(self):
        sg.theme('Reddit')
        column1 = [
            [sg.Radio('Cadastrar receitas', group_id='Receitas', font=("Helvetica", 15), key=self.C_RECEITAS)],
            [sg.Radio('Exibir receitas', group_id='Receitas', font=("Helvetica", 15), key=self.R_RECEITAS)],
            [sg.Radio('Excluir receitas', group_id='Receitas', font=("Helvetica", 15), key=self.D_RECEITAS)]
            ]

        layout = [
            [sg.Column([[sg.Text('Sobre Receitas', font=("Helvetica", 20), pad=((50,200),(30,30)))]], pad=(30, 30))],
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

    def cadastrar_receita(self, imoveis: list[Imovel], plataformas: list[Plataforma]):
        sg.theme('Reddit')

        opcoes_imoveis = [f'{imovel.id} - {imovel.titulo}' for imovel in imoveis]
        opcoes_plataformas = [f'{plataforma.id} - {plataforma.titulo}' for plataforma in plataformas]

        column1 = [
            [sg.Text('Valor: R$ ', font=("Helvetica", 15)), sg.Input(key='valor', size=(56, 1))],
            [sg.Text('Imóvel associado:', font=("Helvetica", 15)), sg.Combo(opcoes_imoveis, key='id_imovel', size=(44, 1), readonly=True)],
            [sg.Text('Plataforma associada:', font=("Helvetica", 15)), sg.Combo(opcoes_plataformas, key='id_plataforma', size=(40, 1), readonly=True)],
            [sg.Text('Observação:', font=("Helvetica", 15)), sg.Input(key='obs', size=(52, 1))],
            [sg.Text('Data:', font=("Helvetica", 15)), sg.InputText('', key="data", size=(61, 1), disabled=True), sg.CalendarButton("Calendário", target="data", format="%d/%m/%Y")],
            [sg.Text('Tags:', font=("Helvetica", 15)), sg.Text('(separadas por vírgula)', font=("Helvetica", 10)), sg.Input(key='tags', size=(40, 1))],
        ]

        layout = [
            [sg.Column([[sg.Text('Cadastrar Receita:', font=("Helvetica", 20))]], pad=(30, 20))],
            [sg.Column(column1, pad=(30, 30))],
            [sg.Button('Voltar', pad=(30, 30), button_color=('white', 'red'), key=self.VOLTAR),
            sg.Button('Confirmar', pad=(0, 30), key=self.PROSSEGUIR)]
        ]
        self.__window = sg.Window('Cadastrar Receita').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        if button == self.PROSSEGUIR:
            id_imovel = values['id_imovel'].split(' - ')[0] if values['id_imovel'] else None
            id_imovel = int(id_imovel) if values['id_imovel'] else None
            id_plataforma = values['id_plataforma'].split(' - ')[0] if values['id_plataforma'] else None
            id_plataforma = int(id_plataforma) if values['id_plataforma'] else None
            data=str(values['data'])
            tags_list = [tag.strip() for tag in values['tags'].split(',') if tag.strip()]
            valor = values['valor'].replace(',', '.') if values['valor'] else None
            obs = values["obs"]
            return valor, id_imovel, id_plataforma, obs, data, tags_list
        else:
            return None, None, None, None, None, None

    def exibir_receitas(self, receitas: list[Receita]):
        sg.theme('Reddit')

        dados = [[receita.valor, receita.imovel.titulo, receita.plataforma.titulo, receita.obs, receita.data, receita.tags, receita.id] for receita in receitas]

        colunas = ['Valor', 'Imóvel', 'Plataforma', 'Observação', 'Data', 'Tags', 'ID']

        layout = [
            [sg.Text('Lista Receitas:', font=("Helvetica", 20), pad=(30, 20))],
            [sg.Table(values=dados, headings=colunas, max_col_width=25, auto_size_columns=True, justification='center',
                      key='table')],
            [sg.Button('Ok', pad=(30, 30), button_color=('white', 'red'), key=self.VOLTAR)]
        ]
        self.__window = sg.Window('RBR Imóveis').Layout(layout)
        button, values = self.__window.Read()
        if button is None or button == 'Ok':
            self.__window.Close()
            return None
        self.__window.Close()
        return None

    # def excluir_receita(self, receitas: list[Receita]):
    #     sg.theme('Reddit')
    #
    #     dados = [[receita.valor, receita.imovel.titulo, receita.plataforma.titulo, receita.obs, receita.data,
    #               receita.tags, receita.id] for receita in receitas]
    #
    #     colunas = ['Valor', 'Imóvel', 'Plataforma', 'Observação', 'Data', 'Tags', 'ID']
    #
    #     layout = [
    #         [sg.Text('Lista Receitas:', font=("Helvetica", 20), pad=(30, 20))],
    #         [sg.Table(values=dados, headings=colunas, display_row_numbers=False,
    #                   auto_size_columns=False, num_rows=min(25, len(dados)), pad=(30, 30),
    #                   col_widths=[10, 20, 20, 20, 15, 15, 15], key='-TABLE-', enable_events=True)],
    #         [sg.Text('Digite o ID da receita que deseja excluir:', font=("Helvetica", 15), pad=(30, 20))],
    #         [sg.Text('ID:', font=("Helvetica", 15), pad=(30, 20)), sg.Input(key='id', pad=(30, 20))],
    #         [sg.Button('Voltar', pad=(30, 30), button_color=('white', 'red')), sg.Button('Excluir', pad=(0, 30))]
    #     ]
    #
    #     self.__window = sg.Window('RBR Imóveis').Layout(layout)
    #
    #     while True:
    #         event, values = self.__window.Read()
    #         if event is None or event == 'Voltar':
    #             self.__window.Close()
    #             return None
    #         elif event == '-TABLE-':
    #             selected_row_index = values['-TABLE-'][0]
    #             selected_receita_id = dados[selected_row_index][6]
    #             self.__window['id'].update(selected_receita_id)
    #         elif event == 'Excluir':
    #             self.__window.Close()
    #             return values['id']

    def excluir_receita(self, receitas: list[Receita]):
        sg.theme('Reddit')

        dados = [[receita.valor, receita.imovel.titulo, receita.plataforma.titulo, receita.obs, receita.data,
                  receita.tags, receita.id] for receita in receitas]

        colunas = ['Valor', 'Imóvel', 'Plataforma', 'Observação', 'Data', 'Tags', 'ID']

        layout = [
            [sg.Text('Lista Receitas:', font=("Helvetica", 20), pad=(30, 20))],
            [sg.Table(values=dados, headings=colunas, display_row_numbers=False,
                      auto_size_columns=False, num_rows=min(25, len(dados)), pad=(30, 30),
                      col_widths=[10, 20, 20, 20, 15, 15, 15], key='-TABLE-', enable_events=True)],
            [sg.Button('Voltar', pad=(30, 30), button_color=('white', 'red')), sg.Button('Excluir', pad=(0, 30))]
        ]

        self.__window = sg.Window('RBR Imóveis').Layout(layout)

        while True:
            event, values = self.__window.Read()
            if event is None or event == 'Voltar':
                self.__window.Close()
                return None
            elif event == '-TABLE-':
                selected_row_index = values['-TABLE-'][0]
                selected_receita_id = dados[selected_row_index][6]
            elif event == 'Excluir':
                self.__window.Close()
                return selected_receita_id


    def close(self):
        self.__window.Close()
        self.__window = None



