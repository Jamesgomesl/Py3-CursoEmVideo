def menu_1var_int(input_text, except_text):
    while True:
        try:
            var = int(input(f'{input_text}:'))
            return var
            break
        except:
            print(f'{except_text}')


print('PyCalculadora de Progressão Aritmética\n')
i, r, t, c = 0, 0, 0, 0
i = menu_1var_int('Digite o primeiro termo da PA', '    somente números inteiros')
r = menu_1var_int('Digite a razão da PA', '    somente números inteiros')
t = menu_1var_int('Quantos números da sequência', '    somente números inteiros')

while True:
    while c < t:
        n = i + r * c
        c += 1
        print(f'{c:02}. {n}')
    user = str(input('Deseja continuar[S/N]?')).strip().upper()
    if user == 'S':
        t += menu_1var_int('Deseja quantas casas a mais', '    somente números inteiros')
    elif user == 'N':
        break
    else:
        print('    opção inválida')
    print()

input('\nENTER para sair')
