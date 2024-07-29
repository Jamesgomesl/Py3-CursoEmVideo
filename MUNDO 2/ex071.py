"""ex071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas células de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$ 1.
"""
# criar DEF arred_2f >> saldo = float(f'{saldo:.2f}')
from random import random

cedulas, a_receber = (50, 20, 10, 1), []
saldo = random() * 1000
nome_primeiro = 'James'
print('{:=^20}'.format(' Banco CeV '))
print(f'Bem vindo, {nome_primeiro}.\nSeu saldo é R${saldo:.2f}')
print('\nO caixa possui cédulas de:')
for valor in cedulas:
    print(f'| R${valor},00 ', end='')
else:
    print('|')

while True:
    try:
        saque = int(input('\nQual o valor a ser sacado: '))
        if saque > saldo:
            print('Erro: Valor de saque maior que o saldo')
            continue
        if saque == 0:
            raise ValueError
        saldo -= saque
        calc = saque
        # Calculo das notas
        for valor in cedulas:
            quantidade = calc // valor
            a_receber.append(quantidade)
            calc = calc % valor
        if calc == 0:
            break
    except ValueError:
        print('Erro: somente números inteiros')
print(f'\nSeu saque de R${saque:.2f} foi autorizado.')
print(f'\nSeu saldo atual é R${saldo:.2f}')
print('\nVocê receberá:')
for c in range(0, len(cedulas)):
    if a_receber[c] != 0:
        print(f'{a_receber[c]} cédulas de R${cedulas[c]:.2f}')

input('\nENTER para sair')
