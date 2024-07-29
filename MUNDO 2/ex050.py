"""ex050: Desenvolva um programa que
 leia seis números inteiros e mostre 
 a soma apenas daqueles que forem pares. 
 Se o valor digitado for impar, 
 desconsidere-o."""
pares = 0
for c in range(1, 6+1):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:  
    # ta dando sintaxe inválida no dois pontos?!
        pares += num
print('A soma dos numeros pares é', pares)