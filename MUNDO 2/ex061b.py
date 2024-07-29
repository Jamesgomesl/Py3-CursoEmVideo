i = int(input('Digite o primeiro termo da PA (número inteiro):'))
r = int(input('Digite a razão da Progressão Aritmética (inteiro):'))
c = 1
n = i
while c <= 10:
    print(f'{c:02}. {n}')
    n += r
    c += 1
