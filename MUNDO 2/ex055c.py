"""ex055: Faça um programa que leia 
o peso de cinco pessoas. No final,
 mostre qual foi o maior e o menor 
 peso lidos."""
def embutir_float(x, y, z):
    for c in range(1, y+1):
        try:x.append(float(input(f'Digite {z} {c}:')))
        except: print('ERRO')

pesos = []
maior, menor = 0, None
embutir_float(pesos, 5, 'peso')

for item in pesos:
    if item > maior:
        maior = item
    if menor == None:
        menor = item
    if item < menor:
        menor = item
print(pesos)
print(f'\nO maior peso foi {maior:.2f}kg'
	f'\ne o menor peso foi {menor:.2f}kg')
