num = int(input('Digite um número inteiro entre 0 e 9999: '))
# StringWAY
num = str(num).zfill(4)
print('''\nAnalisando seu número...\n
      Milhar:  {}
      Centena: {}
      Dezena:  {}
      Unidade: {}
      '''.format(num[0], num[1], num[2], num[3]))
