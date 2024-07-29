tabela = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25.0, 'Transferidor', 4.2, 'Compasso', 9.99,
          'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
largura = 30
print('='*largura)
print(' Listagem de Preços '.upper().center(largura, '-'))
print('='*largura)
# print(f'{tabela[c]}...R${tabela[c+1]:.2f}'.rjust(largura))
for c in range(0, len(tabela), 2):
    print(f'{tabela[c]}'+f'R${tabela[c+1]:.2f}'.rjust(largura-len(str(tabela[c])), '.'))
