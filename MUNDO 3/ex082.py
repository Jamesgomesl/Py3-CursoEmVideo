"""ex082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""


lista_valores_numericos = []
lista_odd_impares = []
lista_even_pares = []

while True:

    #inputs do usuario
    numero_input = input("Digite um número inteiro: ")
    
    #validando
    try:
        novo_valor = int(numero_input)

    except:
        print("valor inválido" + "\n")
        continue
    
    #adicionando valores
    lista_valores_numericos.append(novo_valor)
    if (novo_valor % 2) == 0:  # se o valor for par
        lista_even_pares.append(novo_valor)
    else:
        lista_odd_impares.append(novo_valor)
    
    #quebra do input
    quebrar_loop = False

    if len(lista_valores_numericos)>0:
        while True:
            user_input = input('Deseja adicionar mais valores?[S/N] ')
            if user_input in "Nn":
                quebrar_loop = True
                print()
                break
            elif user_input in "Ss":
                print()
                break
            else:
                print('opção inválida')  # + "\n")
                continue

    if quebrar_loop:
        break

#finalizando

print(f"Foram digitados {len(lista_valores_numericos)} valores")
print(f"os valores digitados foram: ", end="")
for valor in lista_valores_numericos:
    print(f'{valor}, ', end = "")
else:
    if 5 in lista_valores_numericos:
        print("e há o numero 5 na lista")
    else:
        print("e não há o número 5 na lista")


# mostrando valores pares
print(f"os numeros pares foram: ", end="")
for c in range(0, len(lista_even_pares)):
    print(f'{lista_even_pares[c]}', end = "")
    if c+1 < len(lista_even_pares):
        print(f', ', end="")
else:
    print(f'')

print(f"os numeros impares foram: ", end="")
for c in range(0, len(lista_odd_impares)):
    print(f'{lista_odd_impares[c]}', end = "")
    if c+1 < len(lista_odd_impares):
        print(f', ', end="")