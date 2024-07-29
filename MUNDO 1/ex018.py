from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
ang = radians(ang)
print('\nSeno: {:.3f}'
      '\nCosseno: {:.3f}'
      '\nTangente: {:3f}'
      ''.format(sin(ang), cos(ang), tan(ang)))
