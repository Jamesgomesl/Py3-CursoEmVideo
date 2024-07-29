"""ex053: Crie um programa que leia 
uma frase qualquer e diga se ela é 
um palíndromo, desconsiderando os
 espaços."""
frase = str(input('Digite uma frase para saber se é um palíndromo:\n')).strip().upper()
# SUBI NO ÔNIBUS
trab = frase.replace(' ', '')
trab = trab.replace(',', '')
trab = trab.replace('.', '')
# substituir acentos.....
# SUBINOONIBUS
comp = len(trab) # 12 (-1)

# checagem
ctrl = comp - 1 
cont = 0
for l in range(0, comp):
    if trab[l] == trab[ctrl]:
        cont += 1
    ctrl -= 1

if cont == comp:
    result = 'é'
else:
    result = 'não é'
print('A frase {} tem {} letras e {} um palíndromo'
	     ''.format(trab, comp, result))
