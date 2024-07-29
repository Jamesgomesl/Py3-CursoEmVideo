pessoas = [['nome', 'idade', 'sexo'], ]

print('Cadastro Guanabara'.upper())
while True:
    # nome input
    print(f'\n=== Pessoa {len(pessoas)} ===')
    nome = str(input('Nome: ')).strip()
    while True:  # idade input
        try:
            idade = int(input('Idade: '))
            if idade < 0:
                raise ValueError
            break
        except ValueError:
            print('    Erro! Somente numeros inteiros')
    while True:  # sexo input
        sexo = str(input('Sexo[M/F]: ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
    # anexar a lista
    pessoas.append([nome, idade, sexo])
    # question finalle
    while True:
        q = str(input('\nAdicionar mais pessoas[S/N]?')).strip().upper()
        if q in 'SN':
            if q == 'N':
                terminar = True
                break
            if q == 'S':
                terminar = False
                break
    if terminar == True:
        break
    # print()
# Fim do programa/loop
pessoas_maisde18, mulheres_menosde20 = [], []
for pessoa in pessoas[1:]:
    if pessoa[1] > 18:
    	   pessoas_maisde18.append(pessoa[0])  # adicionar o nome a lista
    if pessoa[2] == 'F' and pessoa[1] < 20:
        mulheres_menosde20.append(pessoa[0])  # idem
print(f'\nAo todo foram cadastradas {len(pessoas)-1} pessoas')
print('Das quais {} tem mais de 18 anos'.format(len(pessoas_maisde18), ))
print('E {} são mulheres com menos de 20 anos'.format(len(mulheres_menosde20), ))

for pessoa in pessoas:
    try:
        if printado == True:
            pass
    except NameError:
        print('\nLISTA Pessoas:')
        printado = True
    print(pessoa)

print('\nLISTA Pessoas com mais de 20:', pessoas_maisde18)

print('\nLISTA Mulheres com menos de 20:', mulheres_menosde20)
