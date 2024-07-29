# 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição
# ela aparece a primeira vez e em que posição ela aparece a última vez.
# GG EASY
frase = str(input('Digite uma frase:\n')).strip()  # me sinto tolo de usar str() no input
print('A letra A aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira letra A aparece na posição {}\n'
      'E a última letra A aparece na posição {}'
      ''.format(frase.lower().find('a'),
                frase.lower().rfind('a'))
      )
