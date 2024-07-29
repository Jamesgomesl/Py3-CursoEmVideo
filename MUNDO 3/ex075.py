valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
"""
valores = ()
for n in range(4):
    entrada = input(f'Valor{n+1}:')
    valores = (valores + tuple(entrada))
"""  # com esse código tinha de caçar os valores em string... coisa terrível
print(f'Você digitou os valores {valores}')
print(f'O valor nove aparece {valores.count(9)} vezes')
print(f'Tem um 3 na {valores.index(3)+1}ª posição')
print('Os valores pares foram: \n(', end='')
for value in valores:
    if value % 2 == 0:
        print(f'{value}, ', end='')
else:
    print(')')
# print(f"""0: {0 in valores}
# 2: {2 in valores}
# 4: {4 in valores}
# 6: {6 in valores}
# 8: {8 in valores}""")
