# MATHway
num = int(input('Digite um número inteiro entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('''Analisando seu número...
      Milhar: {3}
      Centena:{2}
      Dezena: {1}
      Unidade:{0}
      '''.format(u, d, c, m))
