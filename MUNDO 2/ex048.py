"""ex048: Faça um programa que calcule
 a soma entre todos os números ímpares
  que são múltiplos de três e que se 
  encontram no intervalo de 1 a 500."""
contador = 0
acumulador = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        print(c)
        contador += 1
        acumulador += c
print('\nExistem {0} números ímpares múltiplos de 3 entre 1 e 500'
      '\nA soma de todos esses {0} números é {1}'.format(contador, acumulador))
