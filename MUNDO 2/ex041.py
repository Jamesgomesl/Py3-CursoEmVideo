"""ex041: A confederação Nacional de Natação precisa de
 um programa que leia o ano de nascimento de um atleta
 e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- acima: MASTER"""

from datetime import date
from time import sleep

ano_atual = 2017 # date.today().year

print("""Bem vindo ao Sistema de Cadastro Autônomo
 da Confederação Nacional de Natação
 """), sleep(.5)
# nome = input('Digite o seu nome completo: ').strip()
# primeiro_nome = nome.split()[0]
# nasc = int(input('Em que ano você nasceu, {}? '.format(primeiro_nome)))
nasc = int(input('Ano de Nascimento: '))
idade = ano_atual - nasc

if idade <= 9:
    classif = 'MIRIM'
elif idade <= 14:
    classif = 'INFANTIL'
elif idade <= 19:
    classif = 'JUNIOR'
elif idade <= 30:
    classif = 'SÊNIOR'
else:
    classif = 'MASTER'

"""
print('O atleta {} tem {} anos.'
      '\nClassificação: {}'
      ''.format(primeiro_nome, idade,
                classif))
"""

print('O atleta tem {} anos.'
      '\nClassificação: {}'
      ''.format(idade, classif))
