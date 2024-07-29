"""ex054: Crie um programa que leia o
 ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas
 ainda não atingiram a maioridade 
e quantas já são maiores."""
anos, idades = [], []
maiores = 0
for c in range(1,7+1):
    anos.append(int(input(f'Digite o ano em que a {c}ª pessoa nasceu: ')))
for item in anos:
    idades.append(2017 - item)  # 2017 = ano do vídeo em curso
for item in idades:
	if item >= 18:
		maiores += 1
print (f'Das idades informadas, {maiores} pessoa(s) é/são maior(es) de idade')
print (f'e {7-maiores} pessoa(s) é/são menor(es) de idade')

input('\nSAIR')
