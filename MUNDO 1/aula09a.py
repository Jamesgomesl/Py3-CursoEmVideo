# FATIAR
frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])

# ANÁLISE
print(frase.count('o'))  # o minúsculo
print(frase.count('O'))  # O maiúsculo
print(frase.upper().count('O'))  # 0
print(len(frase))
f2 = '  Aprendendo Python  '
print(len(f2))
print(len(f2.strip()))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.istitle())
# TRANSFORMAÇÕES
print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Py3')
print(frase)
# DIVISÃO E LISTAS
dividido = (frase.split())
print(dividido)
print(dividido[2])
print(dividido[2][1])
