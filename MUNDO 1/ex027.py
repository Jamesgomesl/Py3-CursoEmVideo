# 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.
nome = input('Qual o seu nome completo?\n').strip()
nome = nome.split()
c = len(nome)
print('O seu primeiro nome é {}\n'
      'O seu último nome é {}'.format(nome[0], nome[c-1]))
