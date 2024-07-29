from random import randint

print('\n=== Descubra o número! ===')
teste = int(input('Tente um número de 0 a 5: '))
sort = randint(0, 5)

if teste == sort:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou... O número era', sort)

input('\nENTER para sair')
