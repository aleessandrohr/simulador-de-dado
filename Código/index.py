from random import randint
from time import sleep
from interface import *

while True:
    linha('Simulador de Dado')
    op = opção()
    if op == 1:
        linha('Gerando Dados')
        for c in range(2):
            print(f'{c+1}º Dado: {randint(0, 6)}')
            sleep(1.5)
    if op == 2:
        linha('FINALIZANDO PROGAMA')
        sleep(1)
        break