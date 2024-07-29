b = 'BINÁRIO'
o = 'OCTAL'
h = 'HEXADECIMAL'
escala_nome = None
final = None

print('Conversor de Bases de Números\n')
num = int(input('Digite um número inteiro: '))
print('\nEscolha entre:'
      '\n[ B ] converter {0} para {1}'
      '\n[ O ] converter {0} para {2}'
      '\n[ H ] converter {0} para {3}'
      ''.format(num, b, o, h))
esc = input('\nDigite a inicial da base para conversão: ').strip().upper()

if esc == 'B':
    final = bin(num)
    escala_nome = b
elif esc == 'O':
    final = oct(num)
    escala_nome = o
elif esc == 'H':
    final = hex(num)
    escala_nome = h
else:
    input('\nVocê não digitou a escala corretamente.'
          '\n\nEnter para sair')
    exit('nao-escala')

print('\n{} em {} é {}'.format(num, escala_nome, final[2:]))
input('\nPressione ENTER para sair')
