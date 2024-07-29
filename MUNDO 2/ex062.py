print('PyCalculadora de Progressão Aritmética')
while True:
    try:
        i = int(input('Digite o primeiro termo da PA:'))
        break
    except: print('    somente números inteiros')
while True:
    try:
        r = int(input('Digite a razão da PA:'))
        break
    except: print('    somente números inteiros')
while True:
    try:
        t = int(input('Quantos números da sequência:'))
        break
    except: print('    somente números inteiros')

c, n = 1, i
while True:
    while c <= t:
        print(f'{c:02}. {n}')
        n += r
        c += 1
    user = str(input('Deseja continuar[S/N]?')).strip().upper()
    if user == 'S':
        while True:
            try:
                q = int(input('Deseja quantas casas a mais:'))
                t += q
                break
            except: print('    somente números inteiros')
    elif user == 'N':
        break
    else:
        print('    opção inválida')
    print()

input('\nENTER para sair')
