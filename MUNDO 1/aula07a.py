# Operadores Aritméticos
print('\nCalculadora Python\n')

n1 = float(input('Digite o primeiro valor: '))
opr = input('Selecione a operação:\n'
            'digite + para soma\n'
            'digite - para subtração\n'
            'digite * para multiplicação\n'
            'digite / para divisão simples\n'
            'digite // para divisão mostrando somente o resultado inteiro\n'
            'digite % para mostrar o resto do resultado da divisão\n'
            'digite ** para potência\n'
            'Operador: ')
n2 = float(input('Digite o segundo valor: '))

# OPERAÇÕES
soma = n1 + n2
subt = n1 - n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
resto = n1 % n2
potn = n1 ** n2  # pow()

# OUTPUTs
print()
if opr == '+':
    print('A soma entre {} + {} é {}'.format(n1, n2, soma))
elif opr == '-':
    print('A subtração de {} - {} é {}'.format(n1, n2, subt))
elif opr == '*':
    print('O produto de {} por {} é {}'.format(n1, n2, mult))
elif opr == '/':
    print('A divisão de {} por {} é {}'.format(n1, n2, div))
elif opr == '//':
    print('A divisão de {} por {} tem o resultado inteiro de {}'
          ''.format(n1, n2, divint))
elif opr == '%':
    print('A divisão de {} por {} tem como resto {}'.format(n1, n2, resto))
elif opr == '**':
    print('A potência de {} elevado a {} é igual a {}'.format(n1, n2, potn))
else:  # nenhum valor compativel de operador
    print('valor incompativel de operador\n')

input('Pressione ENTER para sair')