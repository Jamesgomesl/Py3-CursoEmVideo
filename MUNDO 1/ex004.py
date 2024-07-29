# Autor: James Gomes Lima -- 06/01/2019

# print('O seu texto é: {}'.format(type(texto), ))          -- obsoleto
# if texto is str:                          -- retorna False, o contrário do esperado
# print('Ele é alfanumérico? {}'.format(if texto.isalnum()))   -- subtituido pelo if

texto = input('Digite algo: ')

if texto.__class__(str):
    print('\nO sua entrada é string, como esperado.')
else:
    print('\nWooooow! Você inseriu algo que não é string!\nComo você fez isso??!\n')
    input('pressione ENTER para sair')
    exit()

if texto.isalpha():
    print('É alfabética.')
    if texto.istitle():
        print('E está capitalizada.'
              '\n    Eu gosto quando as coisas estão bem escritas.')
    elif texto.isupper():
        print('E está toda em maiúsculas.'
              '\n    Lembre de desligar o CAPS LOCK quando for escrever. ;)')
    elif texto.islower():
        print('E está em minúsculas.'
              '\n    Ser programador não te permite ser preguiçoso. ;)')
else:
    print('Não é alfabética.')

if texto.isnumeric():
    print('É numérica.')
else:
    print('Não é numérica.')

if texto.isspace():
    print('Por que você digitou somente espaços?')

input('\nObrigado por testar meu primeiro programa Python'
      '\npressione qualquer tecla para encerrar')
