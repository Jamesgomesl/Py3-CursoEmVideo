n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
# TESTE - menor
menor = n1  # reduz o número de testes
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n2 < n2:
    menor = n3
# TESTE - maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# PRINTS
print('O menor número é {}\n'
      'O maior número é {}'.format(menor, maior))
