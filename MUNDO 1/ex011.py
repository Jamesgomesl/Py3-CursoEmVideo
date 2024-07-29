compri = float(input('Qual o comprimento da parede? '))
altura = float(input('Qual a altura da parede? '))
area = compri * altura
tinta = area / 2  # litros
print('A área da parede é {:.2f}m², portanto\n'
      'serão necessários {:.2f} litros de tinta'
      ''.format(area, tinta))
