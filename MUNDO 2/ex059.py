"""ex059: Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em casa caso."""
escolha = 0
a, b = 0, 0
soma, mult = 0, 0
menu = """
[1] Somar
[2] Multiplicar
[3] Maior número
[4] Novos Números
[5] Sair do programa
"""

print('Calculadora Py v2\n')
a = float(input('Digite o 1º número:'))
b = float(input('Digite o 2º número:'))
while True:
    if escolha == 0:  # MENU
        print('{:=^20}'.format(' MENU '))
        print(menu)
        try: escolha = int(input('OPÇÃO:'))
        except TypeError: print('ERROR: Digite um número inteiro')
    if escolha == 1:
        print(f'SOMA = {a+b}')
    if escolha == 2:  # MULT
        print(f'MULTIPLICAÇÃO = {a*b}')
    if escolha == 3:  # MAIOR
        print('MAIOR NÚMERO')
        if a > b:
            print(a, 'é maior que', b)
        if b > a:
            print(b, 'é maior que', a)
        if a == b:
            print(a, 'é igual a', b)
    if escolha == 4:  # NOVOS
        print('\nNOVOS NÚMEROS')
        a = float(input('Digite o 1º número:'))
        b = float(input('Digite o 2º número:'))
    if escolha == 5:  # SAIR
        break
    input()
    escolha = 0
    # fim da elipse

input('\nENTER para sair')
