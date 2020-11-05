def leiaint(número):
    while True:
        try:
            número = int(input(f'{número}'))
        except:
            print(f'\033[31mPor favor digite um número inteiro.\033[m')
        else:
            return número


def linha(msg='', cor='\033[m', fim='\033[m', show=True):
    if show == True:
        print(f'{cor}-' * 42)
        print(msg.center(42))
        print(f'{cor}-{fim}' * 42)
        print('\033[34m1 - Gerar dado')
        print('2 - Sair do progama\033[m')
        print(f'{cor}-{fim}' * 42)
    else:
        print(f'{cor}-' * 42)
        print(msg.center(42))
        print(f'{cor}-{fim}' * 42)


def opção():
    while True:
        opção = leiaint('Sua opção: ')
        if opção == 1:
            return opção
        elif opção == 2:
            return opção
        else:
            print('\033[31mDigite uma opção válida!\033[m')