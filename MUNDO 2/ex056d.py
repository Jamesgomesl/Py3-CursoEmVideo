"""ex056: Deselvolva um programa que leia nome, idade e sexo
 de 4 pessoas.  No final do programa mostre:
  - A média de idade do grupo.
  - Qual é o nome do homem mais velho.
  - Quantas mulheres tem menos de 20 anos."""
from my_defs import teste_sexo


nomes, idades, sexos = [], [], []
n = 4
print()
for c in range(1, n+1):
    nomes.append(input(f'Nome da {c}ª pessoa:'))
    idades.append(int(input(f'Idade da {c}ª pessoa:')))
    sexos.append(teste_sexo())
    #sexos.append(input(f'Sexo da {c}ª pessoa \n(Male or Female):'))
    print()
    
idade_media = 0
for item in idades: idade_media += item
idade_media /= len(idades)  # x/4
print(f'A idade média do grupo é {idade_media:.2f} anos')

maior_idade = 0
for pos in range(0, n):
    if sexos[pos] == 'Male':
        if idades[pos] > maior_idade:
            maior_idade = idades[pos]
            oldest_pos = pos
oldest = nomes[oldest_pos]
print(f'O homem mais velho é {oldest} com {maior_idade} anos')

mulheres_menosde20 = 0
for pos in range (0, n):
    if sexos[pos] == 'Female' and idades[pos] < 20:
        mulheres_menosde20 += 1
print('Das mulheres {} tem menos de 20 anos'.format(mulheres_menosde20, ))
print()

for c in range(0, n):
    print(f'{nomes[c]}, {idades[c]}, {sexos[c]}')
print()

input('ENTER para sair')
