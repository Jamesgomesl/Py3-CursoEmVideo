"""ex058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
 foram necessários para vencer."""
from random import randint

versao = 'v2.2'
minimo, maximo = 0, 9
sorteado = randint(minimo, maximo)
palpite, tentativas = 0, 0
mascara = 'de '+str(minimo)+' a '+str(maximo)

print(' ', '-=' * 14 + '-')
print(' '*5+'Adivinhe o número!', versao)
print(' ', '-=' * 14 + '-')
print(f'\nDescubra qual número eu pensei {mascara}: ')

# repetição / teste
while palpite != sorteado:
    tentativas += 1
    print()
    palpite = int(input('Seu palpite: '))
    if palpite < sorteado:
        if palpite < minimo:
            print(f'O que você está fazendo?!\nSomente números {mascara}')
            tentativas -= 1
        else:
            print('Tente um número maior')
    if palpite > sorteado:
        if palpite > maximo:
            print(f'Até {maximo}, gênio!')
            tentativas -= 1
        else:
            print('Tente um número menor')

# Fim do jogo!
print('=' * 20, )
print('Parabéns, você acertou!')
print(f'TENTATIVAS: {tentativas}')

input('\nENTER para sair')
