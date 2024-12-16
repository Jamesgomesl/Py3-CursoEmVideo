"""ex080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""

lista_valores_numericos = []

while len(lista_valores_numericos)<5:
    print("")
    #inputs do usuario
    user_input = input("Digite um número inteiro: ")

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
        pass

    if len(lista_valores_numericos) == 0:
            lista_valores_numericos.append(novo_valor)
    else:
        adicionado = False
        for n, valor in enumerate(lista_valores_numericos):
            # print(f'{n}. {valor}')
            if novo_valor < lista_valores_numericos[n]:
                lista_valores_numericos.insert(n, novo_valor)
                adicionado = True
                break
        else:
            if not adicionado:
                lista_valores_numericos.append(novo_valor)
            # print()

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