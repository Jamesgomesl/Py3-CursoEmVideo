print('\nTabuada Python v2.0\n')
n = int(input('Insira um número inteiro: '))
z = int(input('Quantas linhas deseja calcular? '))
# c = 1  # controle do while
# while c <= z:
for c in range(0, z+1):
    if c % 10 == 0:
        print('-'*12)
    print('{} * {} = {}'.format(n, c, n * c))
    c += 1
print('-'*12)

input('\nENTER para sair')
