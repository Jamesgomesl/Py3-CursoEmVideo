contador = soma = 0
while True:
    try:
        entrada = int(input('Digite o número para adicionar [999 = stop]: '))
        if entrada == 999: break
        print('    adicionado!')
        contador += 1
        soma += entrada
    except:print('   ERRO! Somente números inteiros')
print(f'\nNo total foram digitados {contador} números cuja soma é {soma}.')

input('\nENTER para sair')
