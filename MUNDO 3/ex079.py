"""ex079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente."""

lista_valores_numericos = []

while True:
    print("")
    #inputs do usuario
    user_input = input("Digite um número inteiro: ")

    if user_input.upper() == "FIM":
        break

    #validando
    try:
        novo_valor = int(user_input)
    except:
        print("valor inválido")
        continue
    
    #inserindo o valor na lista
    if novo_valor in lista_valores_numericos:
        print("valor já existe na lista")
        continue
    else:
        lista_valores_numericos.append(novo_valor)

    #checagem
    terminar_programa = False
    while True:
        checa_continuar = input('Deseja continuar? [S/N]')
        if checa_continuar in 'Nn':
            terminar_programa = True
            break
        elif checa_continuar in 'Ss':
            break
        else:
            continue

    if terminar_programa:
        break

#finalizando
print(f"os valores digitados foram: ", end="")

while True:
    menor_valor = min(lista_valores_numericos)
    posicao_menorvalor = lista_valores_numericos.index(menor_valor)
    print(f"{menor_valor}", end="")
    lista_valores_numericos.pop(posicao_menorvalor)
    
    #controle
    if len(lista_valores_numericos)==0:
        break
    else:
        print(f", ", end="")
