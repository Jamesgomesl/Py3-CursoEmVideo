"""ex038: Escreva um programa que leia dois números inteiros e compare-os,
 mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

print('Comparador de números!')
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))

if num1 > num2:
    print('O PRIMEIRO número é maior')
elif num2 > num1:
    print('O SEGUNDO número é maior')
else:
    print('Os dois números são IGUAIS')
