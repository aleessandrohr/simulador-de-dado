import PySimpleGUI as sg
from time import sleep
from random import randint

class Interface:
    def __init__(self):
        sg.change_look_and_feel('Default1')
        # Layout
        layout = [
            [sg.Button('Gerar dados')],
            [sg.Input(size=(30,0), key='dados')],
            [sg.Output(size=(30,10))]
        ]
        # Janela
        self.janela = sg.Window('Simulador de Dados').layout(layout)


    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            try:
                dado = int(self.values['dados'])
            except:
                pass
            else:
                if dado != 0:
                    c = 1
                    print('-' * 52)
                    while True:
                        print(f'{c}º Dado: {randint(0, 6)}')
                        sleep(0.5)
                        if c == dado:
                            break
                        c += 1
                    print('-' * 52)
tela = Interface()
tela.Iniciar()

