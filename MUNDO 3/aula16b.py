a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
d = a + b
e = b + (1,)
print(c)
print(d)
print(e)
print(e.count(1))  # conta elementos iguais
print(c.index(4))  # procura primeira ocorrencia de tal elemento
print(c.index(5, 1))

pessoa = ('Gustav', 39, 'M', 99.88)  # Mas usar elementos heterogenos
                                     # não era uma vantagem das tuplas??
del pessoa

print(pessoa)
