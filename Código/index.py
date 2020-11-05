from random import randint
from time import sleep
from interface import *

while True:
    linha('Simulador de Dado', cor='\033[33m')
    op = opção()
    if op == 1:
        opc = leiaint('Quantos dados deseja gerar? ')
        linha('Gerando Dados', cor='\033[33m', show=False)
        for c in range(opc):
            print(f'\033[30m{c+1}º Dado: {randint(0, 6)}\033[m')
            sleep(0.5)
    if op == 2:
        linha('FINALIZANDO PROGAMA', cor='\033[31m', show=False)
        sleep(1)
        break