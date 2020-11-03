def leiaint(número):
    while True:
        try:
            número = int(input(f'{número}'))
        except:
            print(f'\033[31mPor favor digite um número inteiro.\033[m')
        else:
            return número


def linha(msg=''):
    print('-' * 42)
    print(msg.center(42))
    print('-' * 42)


def opção():
    print(f'1 - Gerar valor')
    print(f'2 - Sair do progama')
    print('-' * 42)
    while True:
        op = leiaint('Sua opção: ')
        if op == 1:
            return op
        elif op == 2:
            return op
        else:
            print('\033[31mDigite uma opção válida!\033[m')