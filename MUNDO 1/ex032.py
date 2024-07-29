from datetime import date

print('\nCalculadora de Ano Bissexto\n')
ano = int(input(
    'Digite o ano a ser calculado\n'
    'ou digite 0 para o ano atual):'))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de', ano, 'é BISSEXTO')
else:
    print('O ano de', ano, 'não é BISSEXTO')

# Para o ano ser bissexto é preciso que a primeira condição (t1 - teste1)
# seja verdadeira e alguma das outras 2 sejam verdadeiras
t1 = ano % 4 == 0  # multiplo de 4
t2 = ano % 100 != 0  # E não multiplo de 100
t3 = ano % 400 == 0  # OU multiplos de 400

print()
print(' Multiplo de 4:', t1)
print(' Não é multiplo de 100:', t2)
print(' Multiplo de 400:', t3)
input()
