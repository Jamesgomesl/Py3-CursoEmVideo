from random import randint

def rolar_dado(inicio, final):
    return randint(inicio, final)

def gerar_numeros(inicio:int, final:int, quantos:int):
    for c in range (quantos):
        if c == 0:
            lista_numeros = rolar_dado(inicio, final)
        elif c < quantos:
            lista_numeros += rolar_dado(inicio, final)
        elif len(lista_numeros) == quantos:
            return lista_numeros

# tupla = gerar_numeros(0, 99, 5)
tupla = (rolar_dado(0,99), rolar_dado(0,99), rolar_dado(0,99), rolar_dado(0,99), rolar_dado(0,99))
        
print(f"""Tupla: {tupla}
Maior número: {max(tupla)}
Menor número: {min(tupla)}""")
