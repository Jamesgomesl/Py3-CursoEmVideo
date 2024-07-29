r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:  # teste de Triângulo
    print('Essas retas formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:  # RESTOU: dois lados iguais
        print('ISÓCELES!')
else:
    print('Essas retas NÃO podem formar um triângulo!')
# REF: Curso em vídeo ex042 :D
