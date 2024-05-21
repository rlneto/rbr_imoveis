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

class TelaReceitas(Tela):
    C_DESPESAS = "C_DESPESAS"
    R_DESPESAS = "R_DESPESAS"
    D_DESPESAS = "D_DESPESAS"
    PROSSEGUIR = "PROSSEGUIR"
    VOLTAR = "VOLTAR"
    def __init__(self):
        super().__init__()
        self.init_components()



    def init_components(self):
        sg.ChangeLookAndFeel('Reddit')
        layout = [
            [sg.Text('Receitas')],
            [sg.Button('Listar Receitas', key='listar_receitas')],
            [sg.Button('Adicionar Receita', key='adicionar_receita')],
            [sg.Button('Remover Receita', key='remover_receita')],
            [sg.Button('Voltar', key='voltar')]
        ]
        self.__window = sg.Window('RBR Imóveis').Layout(layout)

    def abrir_menu(self):
        button, values = self.__window.Read()
        if button == 'voltar' or button is None:
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

    def cadastrar_receita(self, imoveis, plataformas):

        opcoes_imoveis = [f'{imovel.id} - {imovel.titulo}' for imovel in imoveis]
        opcoes_plataformas = [f'{plataforma.id} - {plataforma.nome}' for plataforma in plataformas]

        column1 = [
            [sg.Text('Valor: R$ ', font=("Helvetica", 15)), sg.Input(key='valor', size=(56, 1))],
            [sg.Text('Imóvel associado:', font=("Helvetica", 15)), sg.Combo(opcoes_imoveis, key='id_imovel', size=(44, 1), readonly=True)],
            [sg.Text('Plataforma associada:', font=("Helvetica", 15)), sg.Combo(opcoes_plataformas, key='id_plataforma', size=(44, 1), readonly=True)],
            [sg.Text('Observação:', font=("Helvetica", 15)), sg.Input(key='obs', size=(52, 1))],
            [sg.Text('Data:', font=("Helvetica", 15)), sg.InputText('', key="data", size=(61, 1), disabled=True), sg.CalendarButton("Calendário", target="data", format="%d/%m/%Y")],
            [sg.Text('Tags:', font=("Helvetica", 15)), sg.Text('(separadas por vírgula)', font=("Helvetica", 10)), sg.Input(key='tags', size=(40, 1))],
        ]

        layout = [
            [sg.Column([[sg.Text('Cadastrar Receita:')]], pad=(30, 20))],
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
            data = str(values['data'])
            tags_list = [tag.strip() for tag in values['tags'].split(',') if tag.strip()]
            valor = values['valor'].replace(',', '.') if values['valor'] else None
            obs = values["obs"]
            return valor, id_imovel, id_plataforma, obs, data, tags_list
        else:
            return None, None, None, None, None, None

    def exibir_receitas(self, receitas):
        dados = [[receita.valor, receita.imovel.titulo, receita.plataforma.nome, receita.obs, receita.data, receita.tags, receita.id] for receita in receitas]
        layout = [
            [sg.Text('Receitas')],
            [sg.Table(values=dados, headings=['Valor', 'Imóvel', 'Plataforma', 'Observação', 'Data', 'Tags'], auto_size_columns=False, col_widths=[10, 20, 20, 20, 20, 20], justification='center', key='table')],
            [sg.Button('Voltar', key='voltar')]
        ]
        self.__window = sg.Window('RBR Imóveis').Layout(layout)
        button, values = self.__window.Read()
        if button is None or button == 'voltar':
            self.__window.Close()
            return None
        self.__window.Close()
        return None

