from my_defs import tabela_cursoemvideo

tabela = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25.0, 'Transferidor', 4.2, 'Compasso', 9.99,
          'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
spacing = 30
print('='*spacing)
print(' Listagem de Preços '.upper().center(spacing, '-'))
print('='*spacing)
tabela_cursoemvideo(tabela, spacing)
