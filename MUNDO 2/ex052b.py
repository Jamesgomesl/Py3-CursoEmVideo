num = int(input('Digite um número inteiro para saber se é primo:'))
primo = True  # condicao a ser testada
div = []
lim = int(num/2)  # Limite

print('\ncalculando...', end='')
for c in range(2, lim):
    if num % c == 0:
        primo = False
        div.append(c)
    print('.', end='')
print('\n')

if num <= 0:
    print('Somente números positivos')
elif num == 1:
    primo = False
    print(num, 'não é primo.')
elif primo == True:
    print(num, 'é primo!')
else:
    print(num, 'não é primo pois ele é divisível por:')
    print(div)

input('\nENTER para sair')
