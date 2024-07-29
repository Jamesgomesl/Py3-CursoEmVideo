# ex078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e qual o menor valor digitado com suas respectivas posições na lista.

lista = list()
for c in range(5):
	valor = int(input(f'VALOR {c}: '))
	lista.append(valor)
print(f'O maior valor foi: {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor foi: {min(lista)} na posição {lista.index(min(lista))}')

input('')
