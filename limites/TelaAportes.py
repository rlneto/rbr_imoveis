from limites.Tela import Tela
import PySimpleGUI as sg 

class TelaAportes(Tela):
    C_APORTES = "C_APORTES"
    R_APORTES = "R_APORTES"
    D_APORTES = "D_APORTES"
    APORTES = "APORTES"
    VOLTAR = "VOLTAR"
    PROSSEGUIR = "PROSSEGUIR"

    def __init__(self):
        super().__init__()
        self.__window = None

    def abrir_menu(self):
        sg.theme('Reddit')
        column1 = [[sg.Radio('Cadastrar aportes', group_id='Aportes', font=("Helvetica", 15), key=self.C_APORTES)],
                   [sg.Radio('Exibir aportes', group_id='Aportes', font=("Helvetica", 15), key=self.R_APORTES)],
                   [sg.Radio('Excluir aportes', group_id='Aportes', font=("Helvetica", 15), key=self.D_APORTES)]]

        layout = [[sg.Text('Sobre Aportes', font=("Helvetica", 20), pad=((50, 200), (30, 30)))],
                  [sg.Column(column1, pad=(30, 30))],
                  [sg.Button('Voltar', key=self.VOLTAR, pad=(20, 20), button_color=('white', 'red')), 
                   sg.Button('Confirmar', key=self.PROSSEGUIR, pad=(0, 20))]]
        
        self.__window = sg.Window('RBR Imóveis').Layout(layout)
        button, values = self.__window.Read()
        if button == self.VOLTAR or button is None:
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

    def cadastrar_aporte(self):
        sg.theme('Reddit')

        layout = [
            [sg.Text('Valor:', font=("Helvetica", 15)), sg.InputText(key='valor')],
            [sg.Text('Data:', font=("Helvetica", 15)), sg.InputText('', key="data", size=(61, 1), disabled=True), sg.CalendarButton("Calendário", target="data", format="%d/%m/%Y")],
            [sg.Text('Observação:', font=("Helvetica", 15)), sg.InputText(key='obs')],
            [sg.Button('Voltar', pad=(30, 30), button_color=('white', 'red'), key=self.VOLTAR),
             sg.Button('Confirmar', pad=(0, 30), key=self.PROSSEGUIR)]
        ]

        self.__window = sg.Window('Cadastrar Aportes').Layout(layout)
        button, values = self.__window.Read()
        self.close()
        if button == self.PROSSEGUIR:
            data = str(values['data'])
            valor = values['valor'].replace(',', '.') if values['valor'] else None
            obs = values["obs"]
            return valor, obs, data
        else:
            return None, None, None

    def exibir_aportes(self, aportes):
        sg.theme('Reddit')

        dados = [[aporte.valor, aporte.obs, aporte.data, aporte.id] for aporte in aportes]

        colunas = ['Valor', 'Observação', 'Data', 'ID']

        layout = [
            [sg.Text('Lista Aportes:', font=("Helvetica", 20), pad=(30, 20))],
            [sg.Table(values=dados, headings=colunas, display_row_numbers=False,
                      auto_size_columns=False, num_rows=min(25, len(dados)), pad=(30, 30), col_widths=[10, 20, 20, 15])],
            [sg.Button('Ok', pad=(30, 30))]
        ]

        self.__window = sg.Window('RBR Imóveis').Layout(layout)
        button, values = self.__window.Read()
        if button is None or button == 'Ok':
            self.__window.Close()
            return None
        self.__window.Close()
        return None

    def excluir_aportes(self, aportes):
        sg.theme('Reddit')

        dados = [[aporte.valor, aporte.obs, aporte.data, aporte.id] for aporte in aportes]

        colunas = ['Valor', 'Observação', 'Data', 'ID']

        layout = [
            [sg.Text('Lista Aportes:', font=("Helvetica", 20), pad=(30, 20))],
            [sg.Table(values=dados, headings=colunas, display_row_numbers=False,
                      auto_size_columns=False, num_rows=min(25, len(dados)), pad=(30, 30),
                      col_widths=[10, 20, 20, 10], key='-TABLE-', enable_events=True)],
            [sg.Text('Digite o ID do aporte que deseja excluir:', font=("Helvetica", 15), pad=(30, 20))],
            [sg.Text('ID:', font=("Helvetica", 15), pad=(30, 20)), sg.Input(key='id', pad=(30, 20))],
            [sg.Button('Voltar', pad=(30, 30), button_color=('white', 'red')), sg.Button('Excluir', pad=(0, 30))]
        ]

        self.__window = sg.Window('RBR Imóveis').Layout(layout)

        while True:
            event, values = self.__window.Read()
            if event is None or event == 'Voltar':
                self.__window.Close()
                return None
            elif event == '-TABLE-':
                if values['-TABLE-']:
                    selected_row_index = values['-TABLE-'][0]
                    selected_aportes_id = dados[selected_row_index][3]
                    self.__window['id'].update(selected_aportes_id)
            elif event == 'Excluir':
                self.__window.Close()
                return values['id']

    def close(self):
        if self.__window:
            self.__window.Close()
            self.__window = None
