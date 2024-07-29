"""ex051: Desenvolva um programa que
 leia o primeiro termo e a razão de
 uma PA. No final, mostre os 10
 primeiros dessa progressão."""
i = int(input('Digite o primeiro termo da PA (número inteiro):'))
r = int(input('Digite a razão da Progressão Aritmética (inteiro):'))
f = i + 9 * r
c = 1
for n in range(i, f+1, r):
    print('{:02}. {}'.format(c, n))
    c += 1