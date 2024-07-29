dist = float(input('Qual a distância da viagem (Km)? '))
"""
if dist < 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
"""
preço = dist * 0.5 if dist < 200 else dist * 0.45
print('Sua viagem custará R${:.2f}'.format(preço))

