nome = input('\nQual é o seu nome? ')
print(nome.upper())
print(nome.lower())
print('Seu primeiro nome é {} e tem {} letras'
      ''.format(nome.split()[0], len(nome.split()[0])))
splited = nome.split()
sem_esp = ''.join(splited)
print('Ao todo seu nome tem {} letras, sem contar os espaços'
      ''.format(len(sem_esp)))
