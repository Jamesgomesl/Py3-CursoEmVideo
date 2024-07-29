"""ex044: Elabora um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 10% de juros"""

from random import random
from time import sleep

print('{:=^33}'.format(' PAGAMENTO '))
# print('='*10+' PAGAMENTO '+10*'=')
# custo = float(input('Digite o valor das compras: R$ '))
custo = random() * 1000

print('Total das compras: R$ {:.2f}'.format(custo)), sleep(.5)
print('\n{:=^33}'.format(' FORMAS DE PAGAMENTO ')), sleep(.5)
print('[A] à vista em dinheiro / débito'), sleep(.5)
print('[B] à vista no cartão de crédito'), sleep(.5)
print('[C] 2x no cartão de crédito'), sleep(.5)
print('[D] de 3x até 12x no cartão'), sleep(.5)

opcoes_pag = ('A', 'B', 'C', 'D')
forma_pag = None
while not forma_pag in opcoes_pag:
    print(), sleep(.5)
    forma_pag = input('Qual é a opção: ').strip().upper()
    if forma_pag in opcoes_pag:
        pass
    else:
        print('    opção inválida')
print()

if forma_pag == 'A':
    print('Pagamento a vista em dinheiro ou débito: 10% de desconto')
    print('O valor final é R$ {:.2f}'.format(custo - (custo * .1)))
    print('O desconto foi R$ {:.2f}'.format(custo * .1))
if forma_pag == 'B':
    print('Pagamento a vista no cartão de crédito: 5% de desconto')
    print('O valor final é R$ {:.2f}'.format(custo - (custo * .05)))
    print('O desconto foi R$ {:.2f}'.format(custo * .05))
if forma_pag == 'C':
    print('em até 2x no cartão: preço normal')
if forma_pag == 'D':
    vezes_teste_num = False
    vezes_tres_a_doze = False
    while not vezes_teste_num and not vezes_tres_a_doze:
        vezes_cartao = input('Parcelado em quantas vezes? ').strip()
        if vezes_cartao.isnumeric():  # Já testa se é inteiro?
            vezes_teste_num = True 
            # Teste de 3 a 12
            vezes_cartao_int = int(vezes_cartao)
            if 3 <= vezes_cartao_int <= 12:
                vezes_tres_a_doze = True
            else:
                vezes_teste_num = False
                print('    opção inválida. De 3 a 12 parcelas')
        else:
            print('    opção inválida. De 3 a 12 parcelas')
    print('3x ou mais no cartão: 10% de juros')

# EXIT
input('\nENTER para sair')
