# Como no video em curso :D
from datetime import date
atual = date.today().year
n = 7  # adição minha - JGL
tot_maiores = 0
for pess in range(1, n+1):
	nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
	idade = atual - nasc
	if idade >= 18:
		tot_maiores += 1
print (f'Das idades informadas, {tot_maiores} pessoa(s) é/são maior(es) de idade')
print (f'e {n-tot_maiores} pessoa(s) é/são menor(es) de idade')

input('\nSAIR')
