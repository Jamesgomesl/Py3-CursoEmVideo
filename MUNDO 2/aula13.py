"""
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
"""

alunos = [0, 1, 2, 3]
for d in range(0, 4):
    alunos[d] = input('Digite o nome do {} aluno:'.format(d+1))
print(alunos)
