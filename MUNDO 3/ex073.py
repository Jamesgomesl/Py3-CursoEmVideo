campeonato_brasileiro = ('Atlético-MG', 'Palmeiras', 'Bragantino', 'Fortaleza', 'Flamengo', 'Internacional',
                         'Corinthians', 'Fluminense', 'Atlético-GO', 'América-MG', 'Cuiabá', 'Athletico-PR',
                         'São Paulo', 'Ceará', 'Bahia', 'Santos', 'Juventude', 'Sport', 'Grêmio', 'Chapecoense')
print(f"""1. Os primeiros colocados do Brasileirão em 29/10/2021 são:
{campeonato_brasileiro[0:5]}
2. Os últimos 4 colocados são:
{campeonato_brasileiro[-4:]} 
3. Os times em ordem alfabética são:
{sorted(campeonato_brasileiro)}
4. E a Chapecoense está na {campeonato_brasileiro.index('Chapecoense') + 1}ª posição""")

# [-4:]>>>>>[-1:-5:-1]
