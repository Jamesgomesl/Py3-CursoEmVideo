from datetime import date
from time import sleep

ano_atual = date.today().year # 2017 no vídeo

print('Sistema de Alistamento digital - SAD', ano_atual)
nasc = int(input('Digite o ano em que você nasceu: '))
print()
sleep(0.2)

idade = ano_atual - nasc
adiantado = 18 - idade
alistamento = nasc + 18
atrasado = idade - 18

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, ano_atual))

if idade < 18:
    print('Ainda faltam {} anos para seu alistamento.'
          '\nSeu alistamento será em {}'
          ''.format(adiantado, alistamento))
elif idade == 18:
    print('Você está na sua época de alistamento!\n'
          'Vamos lá!')
elif idade == 19:
    print('Você está {} ano atrasado no seu alistamento.\n'
          'Cuide disso logo!'.format(atrasado))
else:
    print('Você deveria ter se alistado a {} anos!'
          '\nSeu alistamento foi em {}.'
          '\n\nVocê precisa resolver isso URGENTEMENTE!'
          ''.format(atrasado, alistamento))

sleep(2)
input('\nPressione ENTER para sair')
