def embutir_str(x, y, z):
    for c in range(1, y+1):
        try: x.append(str(input(f'Digite {z} {c}:')))
        except: print('ERRO')


def embutir_int(x, y, z):
    for c in range(1, y+1):
        try: x.append(int(input(f'Digite {z} {c}:')))
        except: print('ERRO')


def embutir_float(x, y, z):
    for c in range(1, y+1):
        try: x.append(float(input(f'Digite {z} {c}:')))
        except: print('ERRO')


def fatiar_2 (x, y):
    print(f'{x}:', y[2:])
# fatiar_2('HEXADECIMAL', hex(int(input('Digite o número:'))))


def teste_sexo():
    sexos = ('M', 'F')
    while True:
        user_input = str(input('Sexo[M/F]: ')).strip().upper()
        if user_input in sexos: break
        else: print('opção inválida')
    return user_input


def numint_to_pontinhos(number):
    num_orgnz = []
    str_num = str(number)
    for c in range(1, len(str_num)+1, ):
        num_orgnz.append(str_num[-c])
        if c % 3 == 0 and c < len(str_num):
            num_orgnz.append(",")  # ponto ou virgula
    num_orgnz.reverse()
    num_final = ''
    for item in num_orgnz:
        num_final += item
    return num_final


def tabela_cursoemvideo(tabela, largura: int):
    """ Dado uma listagem em sequencia de produtos/preço, ambientes/areas..
    Gera uma tabela de largura N (int)
    """
    for c in range(0, len(tabela), 2):
        print(f'{tabela[c]}' + f'R${tabela[c + 1]:.2f}'.rjust(largura - len(str(tabela[c])), '.'))

# END
