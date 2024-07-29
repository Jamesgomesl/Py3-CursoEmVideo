#ex60: fatorial
print('Py Fatorial\n')
while True:
    try:
        num = int(input('Número: '))
        break
    except: print('somente números inteiros')

c = num - 1
fat = num
print(f'{num}! = {num}', end = '')

while c > 0:
    print(f' * {c}', end = '')
    fat *= c
    c -= 1
print(' =', fat)
# fim
