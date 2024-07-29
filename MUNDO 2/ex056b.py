n = 4
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20menos = 0

for p in range(1, n+1):
	print(f'----- {p}ª PESSOA -----')
	nome = str(input('Nome: ')).strip()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo [M/F]: ')).strip()  # Vai corrigir direto no IF
	soma_idade += idade
	if p == 1 and sexo in 'Mm':  # Aqui
		maior_idade_homem = idade
		nome_velho = nome
	if sexo in 'Mm' and idade > maior_idade_homem:
		maior_idade_homem = idade
		nome_velho = nome
	if sexo in 'Ff' and idade < 20:
		total_mulher_20menos += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo {total_mulher_20menos} mulheres tem menos de 20 anos.')

input('\nSAIR')
