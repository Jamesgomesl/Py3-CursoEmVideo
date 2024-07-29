numeros_de_0_a_20 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    try:
        num = int(input('\nDigite um número de 0 a 20: '))
        if num < 0 or num > len(numeros_de_0_a_20) -1:  # -1 por conta do zero ;)
            raise ValueError
        print(f'\n    Você digitou o número {numeros_de_0_a_20[num]}')
    except ValueError:
        print('    Inválido')
    except TypeError:  # nunca caiu em TypeError
        print('ERRO! Digite um número inteiro')
