print('Programa PyTABUADA')

while True:
    try:
        num = int(input('\nTABUADA DE '))
        if num < 0:
            break
        #tabuada em si
        print('-'*12)
        for line in range(10):
            print(f'{line+1:2} * {num:2} = {(line+1)*num:2}')
        print('-'*12)
    except ValueError:
        print('ERRO! Somente números inteiros.')
    except:
        break
print('\nPROGRAMA PyTABUADA ENCERRADO')
input('\nFIM')
#end