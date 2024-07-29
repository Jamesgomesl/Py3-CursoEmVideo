a, b, f, count = 0, 1, 1, 1

print('{:=^40}'.format(' Fibonacci '))

while True:
    try:
        end = int(input('Quantas casas da sequência: '))
        break
    except:
        print('    somente números inteiros')
    print()

while count < end:
# for count in range(1, end+1):
    count += 1
    f = a + b
    print(f'{count:0>2}. {f}')
    a = b
    b = f
