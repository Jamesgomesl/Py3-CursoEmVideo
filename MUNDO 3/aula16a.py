#   "As tuplas são IMUTÁVEIS"     (durante a execução do programa, dãã)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
# ambas as tuplas são idênticas! Sem diferenças. Dá para definir de ambas maneiras

# Tuplas aceitam fatiamento (mas não alterações "in run")

""" Maneiras de imprimir todos os itens em uma coleção(tupla): """
# Maneira 1: "varrendo"
for comida in lanche:
    print(f'Eu vou comer {comida}')
else:
    print()

# Maneira 2: método 'range'
for cont in range(0, len(lanche)):
    print('Eu vou comer {}'.format(lanche[cont]))
else:
    print()

# Maneira 3: método 'range' usando posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
else:
    print()

# Maneira 4: método 'enumerate'
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {lanche[pos]} na posição {pos}')
else:
    print()

print('Comi pra caramba!\n')

# Outro método
print(sorted(lanche))  # SORTED = ordem alfabética
print(lanche)
