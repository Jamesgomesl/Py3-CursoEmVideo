# ex077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

vegetais = ('---------', 'banana', 'abobora', 'tomate', 'cebola', 'alface', 'rucula', 'beterraba', 'açai', )
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
colecao = palavras + vegetais
print(type(colecao))
vogais = ('a', 'e', 'i', 'o', 'u')
for word in colecao:
    print(f'{word.upper()} -- Vogais: ', end='')
    for letter in vogais:
        if letter.upper() in word.upper():
            print(letter.upper(), end=' ')
    print()
