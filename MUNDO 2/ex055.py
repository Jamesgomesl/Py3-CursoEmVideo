"""ex055: Faça um programa que leia 
o peso de cinco pessoas. No final,
 mostre qual foi o maior e o menor 
 peso lidos."""
pesos = []
maior, menor = 0, None
for c in range(1, 5+1):
    try:pesos.append(float(input(f'Digite o {c}º peso:')))
    except: print('ERRO')
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
