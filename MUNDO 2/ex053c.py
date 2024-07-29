# Forma 1 - como no vídeo
frase = str(input('Digite uma frase para saber se é um palíndromo:\n')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')

input('SAIR')
