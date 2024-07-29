"""ex043: Desenvolva uma lógica que leia o peso e altura de uma pessoa,
 calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""

peso = float(input('Qual é o seu peso(kg): '))
altura = float(input('Qual é a sua altura(m)? '))

IMC = peso / (altura ** 2)

print('\nO seu IMC é {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif IMC < 25:
    print('Parabeéns, você está na faixa de PESO IDEAL!')
elif IMC < 30:
    print('Você está com SOBREPESO.')
elif IMC < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

input('\nENTER para sair')
