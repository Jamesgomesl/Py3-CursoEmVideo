# Variáveis Compostas: LISTAS 1/2

"""Minhas anotações"""

# declaração
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

# alterar elementos
lanche[3] = 'picolé'

# adicionar elementos ao final uma lista
lanche.append('cookie')

# adicionar elementos em qualquer posição
lanche.insert(0, 'cachorro-quente')

# remover elementos de uma lista
lanche.remove('pizza')  # remover através do elemento em si
del (lanche[3])  # remover elemento na posição n
lanche.pop(3)  # remove o ultimo elemento se não for indicado uma posição

print(lanche)
