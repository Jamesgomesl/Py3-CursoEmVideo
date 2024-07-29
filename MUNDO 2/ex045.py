# ex045: Crie um programa que faça o computador jogar Jokenpô com você

from random import choice
from time import sleep

# ABERTURA
print('GAME: ', end='')
sleep(.5)
print('Jo ', end='')
sleep(.5)
print('Ken ', end='')
sleep(.5)
print('Pô')

# VARIAVEIS e LISTA
rodada = 0
pontos = 0
JoKenPo = ('PEDRA', 'PAPEL', 'TESOURA')

# JOGO
while rodada < 3:
    print(), sleep(.5)
    rodada += 1
    print('RODADA {}/3'.format(rodada))
    sleep(.5)
    escolha = input('PEDRA, PAPEL ou TESOURA?\n').strip().upper()
    # escolher
    sort = choice(JoKenPo)
    # teste do input
    if escolha in JoKenPo:
        sleep(.5), print(sort)
    else:
        print('   opção inválida! Tente novamente')
        rodada -= 1
    # testes e pontos!
    if escolha == sort:
        print(' EMPATE      PONTOS:', pontos)
    else:
        if escolha == 'PEDRA' and sort == 'PAPEL':
            print(' PERDEU      PONTOS:', pontos)
        if escolha == 'PEDRA' and sort == 'TESOURA':
            pontos += 1
            print(' GANHOU      PONTOS:', pontos)
        if escolha == 'PAPEL' and sort == 'PEDRA':
            pontos += 1
            print(' GANHOU      PONTOS:', pontos)
        if escolha == 'PAPEL' and sort == 'TESOURA':
            print(' PERDEU      PONTOS:', pontos)
        if escolha == 'TESOURA' and sort == 'PEDRA':
            print(' PERDEU      PONTOS:', pontos)
        if escolha == 'TESOURA' and sort == 'PAPEL':
            pontos += 1
            print(' GANHOU      PONTOS:', pontos)
# FIM DA SEÇÃO Jogo

print('\n     FIM DE JOGO     PONTOS:', pontos)
sleep(1)
input('\nENTER para sair')
