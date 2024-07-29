salario = float(input('Qual o seu salário atual? R$ '))
if salario <= 1250:
    percent = 15  # 15% ou .15
else:
    percent = 10  # 10% ou .1
final = salario + salario * (percent/100)
print('O seu aumento será de {}%\n'
      'O salário passa a ser R$ {:.2f}'.format(percent, final))
