# ex036: Escreva um programa para aproveitar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
from math import ceil

print('\nQualquerBANK'), sleep(.3)
print('Simulador de Financiamento Residencial\n'), sleep(.3)

casa = float(input('Quanto custa a sua casa pretendida? R$ '))
if casa < 1000:
    casa *= 1000

renda = float(input('Quanto é a sua renda mensal R$ '))
if renda < 100:
    renda *= 1000

tempo = input('Em quanto tempo você deseja pagar? (?m ou ?a): ')
if 'a' in tempo:  # identar se ativar a linha superior
    pos_a = tempo.lower().find('a')
    tempo = tempo[0:pos_a]
    meses = 12 * int(tempo)
else:
    meses = tempo

sleep(.5), print()

# calculo de viabilidade
mensal = casa / meses
limite = renda * .3  # 30%

# Calculo inverso - caso nao seja aprovado
renda_ideal = mensal * 100 / 30  # renda dado o custo mensal (inverso de 30%)
tempo_ideal = ceil(casa / limite)  # Quantos meses com essa renda/limite
# calculo de meses e anos arredondados
ideal_anos = tempo_ideal // 12
ideal_meses = tempo_ideal % 12

# TABELA
print("""Seu limite de investimento: R$ {:.2f} (30% da renda)
Custo mensal do financiamento: R$ {:.2f}
""".format(limite, mensal))

sleep(1.5)

if mensal <= limite:
    print('Seu financiamento poderá ser aprovado.')
    print('O prazo ideal de conclusão do financiamento é', tempo_ideal, 'meses')
    if tempo_ideal > 12:
        print('ou seja, {} ano(s) e {} mês(es)'.format(ideal_anos, ideal_meses))
    print('\nBoa sorte!')
else:
    print('Infelizmente, seu financiamento NÃO será aprovado.')
    print('Deseja calcular as possibilidades mantendo a sua RENDA ou o PRAZO escolhido?\n')
    escolha: str = input('Escolha entre as 2 opções acima ou deixe em branco para encerrar: ')
    if escolha.upper() == 'R' or 'RENDA':
        print('\nCom R$ {:.2f} de renda o prazo mínimo é de {} meses'.format(renda, tempo_ideal))
        if tempo_ideal > 12:
            print('ou seja {} ano(s) e {} mês(es)'.format(ideal_anos, ideal_meses))
    elif escolha.upper() == 'P' or 'PRAZO':
        print('\nMantendo o prazo de {} meses, a sua renda deve ser R$ {:.2f}'
              '\npara atender ao limite máximo de comprometimento de renda (30%)'
              ''.format(meses, renda_ideal))
    elif escolha == '':
        print('\nEntendemos a frustração e que não queira tentar novamente'
              '\nMas esperamos que você consiga o sonho da sua casa própria!')
    else:
        print('\nVocê digitou algo incorreto.'
              '\nSe precisar, execute o programa novamente!')

sleep(2)
input('\nQualquerBANK agradece a preferência\n'
      '\nPressione ENTER para sair')
