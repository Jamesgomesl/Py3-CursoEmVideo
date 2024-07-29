"""ex042: Refaça o ex035 (dos triângulos), acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados são iguais
- Isóceles: dois lados são iguais
- Escaleno: todos os lados são diferentes
Ver ex035 """

print('-='*15+'-')
print('  Analizador de Triângulos 2.0')
print('-='*15+'-\n')

# feito por JamesGL e somente por JGL - sem consulta!!!

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

texto_isoceles = 'Essas retas PODEM formar um triângulo ISÓCELES'

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  # teste de Triângulo
    if r1 == r2 and r2 == r3:
        print('Essas retas formam um triângulo EQUILÁTERO')
    elif r1 == r2 and r1 != r3:
        print(texto_isoceles)
    elif r1 == r3 and r1 != r2:
        print(texto_isoceles)
    elif r2 == r3 and r3 != r1:
        print(texto_isoceles)
    else:
        print('Essas retas formam um triângulo ESCALENO')
else:
    print('Essas retas NÃO podem formar um triângulo')

input('\nENTER para sair')
