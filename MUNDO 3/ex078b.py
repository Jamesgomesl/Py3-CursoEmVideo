# ex078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista_num.
# No final, mostre qual foi o maior e qual o menor valor digitado com suas respectivas posições na lista_num.

lista_num = list()
for c in range(5):
	valor = int(input(f'VALOR {c}: '))
	lista_num.append(valor)

valor_maior = max(lista_num)
valor_menor = min(lista_num)

print(f'O maior valor foi: {valor_maior} na posição ', end="")
for m in lista_num:
	if m == valor_maior:
		print(f'{m}.. ')

print(f'O menor valor foi: {valor_menor} na posição ', end="")
for n in lista_num:
	if n == valor_menor:
		print(f'{n}.. ')

input('')
