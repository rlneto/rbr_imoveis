from limites.Tela import Tela
import PySimpleGUI as sg

class TelaCaixa(Tela):
    def exibir_caixa(self, caixa = 0):
        sg.theme('Reddit')

        layout = [
            [sg.Text('Total em caixa:', font=("Helvetica", 20), pad=(30, 20))],
            [sg.Text(f'R$ {caixa}', font=("Helvetica", 20), pad=(30, 20))],
            [sg.Button('Voltar', pad=(30, 30))]
        ]

        self.__window = sg.Window('RBR Imóveis').Layout(layout)
        button, values = self.__window.Read()
        if button is None or button == 'Ok':
            self.__window.Close()
            return None
        self.__window.Close()
        return None