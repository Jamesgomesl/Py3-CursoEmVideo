"""ex052: Faça um programa que leia um
 número inteiro e diga se ele é ou não
  um número primo."""
num = int(input('Digite um número inteiro para saber se é primo:'))
primo = True  # condicao a ser testada
div = []
for c in range(2, num):
    if num % c == 0:
        primo = False
        div.append(c)
    print('.', end='')
print()
if primo == True:
    print(num, 'é primo!')
else:
    print(num, 'não é primo pois ele é divisível por:')
    print(div)

input('SAIR')
