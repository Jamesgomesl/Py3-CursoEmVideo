from math import hypot
c1 = float(input('Digite o 1º cateto: '))
c2 = float(input('Digite 0 2º catet0: '))
hyp = hypot(c1, c2)
print('A hipotenusa formada pelos catetos {} e {} é {:.2f}'
      ''.format(c1, c2, hyp))
