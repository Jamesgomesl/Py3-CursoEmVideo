"""
O primeiro 'programa' que eu fiz. Fiquei muito feliz em realmente
automatizar uma função. Usei conhecimento de while obtido de uma
outra plataforma. Curso em Video só ensinou isso mais tarde.
E como sempre, eu adiantado sempre tento fazer mais do que o
exercício pede.. :D -- JGL 2019
"""

print('\nTabuada Python\n')
n = int(input('Insira um número inteiro: '))
z = int(input('Quantas linhas deseja calcular: '))
c = 1  # controle
# while c <= z:
for c in range(1, z+1):
    if c == 1:
        print(12*'-')
    print('{} * {} = {}'.format(n, c, n * c))
    c += 1
print(12*'-')

input('\nPressione ENTER para sair')
# eu sempre insiro essa função no final porque sem isso o prompt simplesmente fecharia
