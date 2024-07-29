from time import sleep

num_produtos, custo = 0, 0
lista_nomes_produtos, lista_precos_produtos = [], []
fechar = False
while True:
    try:
        print(f'\n== PRODUTO {num_produtos+1:02} ==')
        nome_produto = str(input('PRODUTO: '))
        if nome_produto == 'FECHAR':
            fechar = True
        else:
            fechar = False

        if not fechar:
            preco_produto = float(input('PREÇO: R$ '))
            if preco_produto < 0:
                raise ValueError

            lista_nomes_produtos.append(nome_produto)
            lista_precos_produtos.append(preco_produto)
            num_produtos += 1

    except ValueError:
        print('     ValueError')
    except TypeError:
        print('     TypeError')

    """
    fechar = False
    if num_produtos > 0:
        while True:
            q = str(input('\nDeseja fechar a nota[S/N]? ')).upper()
            if q == 'N':
                break
            if q == 'S':
                fechar = True
                break
    """
    if fechar:
        break
# CALCULOS
mais_de_mil = 0  # contar quantos produtos custaram ...
mais_barato = 0  # preço do produto ...
nome_produto_mais_barato = 'nenhum'

for cont, preco in enumerate(lista_precos_produtos):
    if mais_barato == 0 or preco < mais_barato:
        mais_barato = preco
        nome_produto_mais_barato = lista_nomes_produtos[cont]
    if preco > 1000:
        mais_de_mil += 1
    custo += preco

# PRINTs
print("""
=== MERCADO GUANABARA ===
  === CUPOM FISCAL ===
"""), sleep(.5)
for cont, produto in enumerate(lista_nomes_produtos):
    print(f"""{cont+1:02}. {produto}
    R$ {lista_precos_produtos[cont]:.02f}
    """)
    sleep(.5)
else:
    print(f'Total a pagar: R$ {custo:.02f}')
sleep(2)
print(f"""
=== MERCADO GUANABARA ===
 === RELATÓRIO FINAL ===
    
    Dos {num_produtos} produtos, {mais_de_mil} custaram mais de R$ 1000
    O produto mais barato foi {nome_produto_mais_barato}, que custou R$ {mais_barato:.02f}
""")

input("""==================================================

                ENTER para sair""")
