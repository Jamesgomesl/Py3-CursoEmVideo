i = int(input('Digite o primeiro termo da PA (número inteiro):'))
r = int(input('Digite a razão da Progressão Aritmética (inteiro):'))
c = 0

# for n in range(i, f+1, r):
while c < 10:
    # if c == 1: n = i
    n = i + r * c
    c += 1
    print(f'{c:02}. {n}')
    