from random import randint


def gerar_numeros():
    return randint(0, 99)


tupla = (gerar_numeros(), gerar_numeros(), gerar_numeros(), gerar_numeros(), gerar_numeros())
print(f"""Tupla: {tupla}
Maior número: {max(tupla)}
Menor número: {min(tupla)}""")
