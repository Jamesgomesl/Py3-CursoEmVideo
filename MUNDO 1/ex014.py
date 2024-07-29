print('\nConversor de Celsius para Fahrenheit\n')

escala_1 = input('Digite a inicial da primeira escala: ')
temp_1 = float(input('Digite a sua temperatura: '))
escala_2 = input('Digite a inicial da segunda escala: ')

if escala_1 == 'C':
    if escala_2 == 'F':
        C_to_F = temp_1 * 9 / 5 + 32
        temp_2 = C_to_F  # 30 - 86
        print('\nConversão de Celsius para Fahrenheit\n'
              '{} °C = {} °F'.format(temp_1, temp_2))
    if escala_2 == 'K':
        C_to_K = temp_1 + 273.15  # C >> K
        temp_2 = C_to_K
        print('\nConversão de Celsius para Kelvin\n'
              '{} °C = {} K'.format(temp_1, temp_2))

if escala_1 == 'F':
    if escala_2 == 'C':
        print('')
    if escala_2 == 'K':
        print('')

if escala_1 == 'K':
    if escala_2 == 'C':
        print('')
    if escala_2 == 'F':
        print('')

input('\nPressione ENTER para sair')
