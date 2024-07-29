'''Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi
alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
por dia e R$0,15 por Km rodado.'''

print('\nLIMA Locadora de Veículos'
      '\nCalculadora de custos'
      '\n')
dias = int(input('Dias de aluguel: '))
km = float(input('Km rodados: '))
custo = km * 0.15 + dias * 60
print('O valor a pagar é R$ {:.2f}'.format(custo))
