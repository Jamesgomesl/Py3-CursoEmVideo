""" ex081: Crie um programaque vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista. """

lista_valores_numericos = []

while True:

    #inputs do usuario
    numero_input = input("Digite um número inteiro: ")
    
    #validando
    try:
        novo_valor = int(numero_input)

    except:
        print("valor inválido" + "\n")
        continue
    

    lista_valores_numericos.append(novo_valor)

    """
    #inserindo o valor na lista
    if novo_valor in lista_valores_numericos:
        print("valor já existe na lista")
        continue
    else:
        pass
    """

    #quebra do input
    quebrar_loop = False

    if len(lista_valores_numericos)>1:
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
