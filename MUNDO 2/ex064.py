"""ex064: Crie um programa que leia vários 
números inteiros pelo teclado. O programa 
só vai parar quando o usuário digitar o valor 
999, que é a condição de parada. No final, 
mostre quantos números foram digitados 
e qual foi a soma entre eles (desconsiderando 
o flag)."""

print('ex064: SOMADORA')
print('Digite números para adicionar a soma.')
print('Basta entrar com 999 para parar o programa')
soma, c, entrada = 0, 0, 0
while True:
    try:
        entrada = int(input('\nNúmero:'))
        if entrada == 999:
            print('STOP!\n')
            break
        soma += entrada
        print('Adicionado!')
        c += 1
    except: print('ERROR! somente números inteiros')
print(f'Ao total foram entrados {c} números, cuja soma é {soma}')
