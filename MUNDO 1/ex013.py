print('\nAtualizador de Salários\n')
s = float(input('Insira o salário atual: R$ '))
p = float(input('Defina o aumento (em %): '))
p /= 100  # transformando em % a variavel
ns = s + (s * p)
a = ns - s
print('O novo salário é R$ {:.2f}\n'
      'O aumento corresponde a R$ {:.2f}'.format(ns, a))
