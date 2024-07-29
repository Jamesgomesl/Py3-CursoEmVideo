print('\nCalculadora de Câmbio\n')
reais = float(input('Insira o valor em reais: R$'))
moeda = input('Qual moeda deseja converter: ')
cot = float(input('Insira a cotação: '))

simp = reais / cot
intt = reais // cot

print('\nVocê pode comprar {}{:.2f}'.format(moeda, simp))
