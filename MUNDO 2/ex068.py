from random import randint

divisoria = '-='*12+'-'

print(divisoria)
print('  DESAFIO PAR ou ÍMPAR')
print(divisoria)
while True:
    # Primeiro INPUT - Número
    while True:
        try:
            jogad_num = int(input('Escolha um número (0-9): '))
            if jogad_num < 0 or jogad_num > 9:
                print('     ERRO! Somente números de 0 a 9')
            else:
                compt_num = randint(0, 9)
                break
        except ValueError:
            print('     ERRO! Somente números inteiros')
    # Segundo INPUT - Par/Ímpar
    while True:
        jogador = str(input('Par ou Ímpar[P/I]: ')).strip().upper()
        if jogador == 'P':
            jogad_aposta = 0  # par
            break
        elif jogador == 'I':
            jogad_aposta = 1  # ímpar
            break
        else:
            print('     ERRO! Escolha: P para PAR ou I para ÍMPAR')
    # SISTEMA
    total = jogad_num + compt_num
    # result
    if total % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    # status
    if total % 2 == jogad_aposta:
        status = 'GANHOU'
    else:
        status = 'PERDEU'
    # PRINTs
    print(divisoria)
    print(f'Você jogou {jogad_num} e o computador {compt_num}\n'
          f'O total é {total}, {result}.\n'
          f'Você {status}!')
    print(divisoria)
    # Reiniciar
    while True:
        q = str(input('Deseja jogar novamente(S/N)? ')).strip().upper()
        if q == 'N':
            parar = True
            break
        if q == 'S':
            parar = False
            break
    if parar:
        break
