"""
ex083: Crie um programa onde o usuário digite uma expressão [MATEMÁTICA] qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos ou fechados na ordem correta.
"""
def contar_parenteses(entrada_expressao):
    parenteses_de_abrir = 0
    parenteses_P_fechar = 0
    for letter in entrada_expressao:
        if letter == "(":
            parenteses_de_abrir += 1
        elif letter == ")":
            parenteses_P_fechar += 1
    
    #returns
    if (parenteses_de_abrir == 0) and (parenteses_P_fechar == 0):
        return "ZERO"
    elif parenteses_P_fechar == parenteses_de_abrir:
        return "IGUAL"
    else:  # numero de parenteses desigual
        return "DESIGUAL"

    
def checar_parenteses(expressao_entrada):
    lista_parenteses = []
    for letter in expressao_entrada:
        if letter == "(":
            lista_parenteses.append(letter)
        elif letter == ")":
            lista_parenteses.append(letter)
    # checagem
    p_de_abrir = 0
    p_de_fechar = 0
    for valor in lista_parenteses:
        if p_de_abrir == 0 and p_de_fechar > 0:
            return "ORDEM INVALIDA"
        elif p_de_fechar > p_de_abrir:
            return "ORDEM INVALIDA"
        elif valor == "(":
            p_de_abrir += 1
        elif valor == ")":
            p_de_fechar += 1
    else:
        return "TUDO CERTO"


# START
texto_de_entrada = "Digite uma expressão numérica para analizar"
print(f"{texto_de_entrada}")

while True:
    #coletar dados
    print()
    expressao_usuario = str(input(f'Expressão: '))
    
    # checagens
    parenteses_iguais = contar_parenteses(expressao_usuario)
    
    if parenteses_iguais == "IGUAL":
        print("O número de parenteses é igual")
        # seguir_testando = True
    elif parenteses_iguais == "DESIGUAL":
        print('Numero desigual de parenteses')
        seguir_testando = False
        continue
    elif parenteses_iguais == "ZERO":
        print("NÃO HÁ PARENTESES")
        continue

    # if seguir_testando:
    checagem = checar_parenteses(expressao_usuario)
    if checagem == "ORDEM INVALIDA":
        print(checagem)
    if checagem == "TUDO CERTO":
        print(checagem)