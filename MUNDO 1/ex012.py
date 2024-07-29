p = float(input('Digite o preço: R$ '))
d = float(input('Digite o desconto (em %): '))
d /= 100
f = p - (p * d)  # preço final
a = (p-f)  # aumento
print('\nO preço final é R$ {:.2f}\n'
      'O desconto corresponde a R$ {:.2f}'.format(f, a))
