print('\nCalculadora de Multas')
vel = float(input('Digite a velocidade (Km/h): '))
lim = 80  # Km/h -- limite
multa = (vel - lim) * 10 // 10 * 7
if vel > lim:
    print('\nVocê estava acima da velocidade permitida: {}Km/h\n'
          'Sua multa será R$ {:.2f}\n'
          'Dirija com mais prudência.'.format(lim, multa))
else:
    print('\nVocê não estava acima da velocidade máxima permitida: {}Km/h\n'
          'Logo, você não foi multado.\n'
          'Dirija sempre com prudência.'.format(lim))
