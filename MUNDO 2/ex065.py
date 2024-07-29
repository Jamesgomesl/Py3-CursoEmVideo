"""ex065: Crie um programa que leia
 vários números inteiros pelo teclado.
 No final da execução, mostre a média
 entre todos os valores e qual foi o
 maior e o menor valores lidos. O
 programa deve perguntar ao usuário
 se ele quer ou não continuar a digitar
 valores."""
c, soma, menor, maior = 0, 0, 0, 0
print('ex065: SOMADORA v1.2')
while True:
    if c > 2:
        q = str(input('\n'+'Adicionar mais números?[S/N]:')).strip().upper()
        if q == 'N':
            break
        elif q == 'S':
            pass
        else:
            print('entrada inválida')
    try:
        num = int(input('\n'+'Número:'))
        print('adicionado!')
        c += 1
        soma += num
        if menor == 0:
            menor = num
        if menor > num:
            menor = num
        if num > maior:
            maior = num
    except:
        print('ERRO, somente números inteiros')
print(f"""
Ao todo foram adicionados {c} números
A média entre eles é de {soma/c}
O maior foi {maior} e o menor foi {menor}
""")
