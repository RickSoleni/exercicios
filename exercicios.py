"""Exercício 1."""
a = [1, 3, 4, 5]
sum(a)

"""Exercício 2."""
listanova = []
lista = [2, 2, 3, 4]
total = 1
for item in lista:
    total = total * item
    listanova.append(total)

"""Exerício 3."""
lista = [2, 1, 123, 52]
maior = lista[0]
for item in lista:
    if item > maior:
        maior = item

print(maior)

"""Exercício 4."""
lista = [2, 1, 123, 52]
menor = lista[0]
for item in lista:
    if item < menor:
        menor = item

print(menor)
