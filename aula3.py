import math


def delta(a, b, c):
    """Retorna o valor de delta."""
    resultado = (b ** 2) - (4 * a * c)
    if resultado <= 0:
        return
    else:
        return resultado


def bhaskara(a, b, c):
    """Retorna o valor das raizes baseadas no delta."""
    rdelta = delta(a, b, c)
    if not rdelta:
        print('Equação impossível de resolver')
        return
    else:
        raiz1 = (-b - (math.sqrt(rdelta))) / (2 * a)
        raiz2 = (-b + (math.sqrt(rdelta))) / (2 * a)
        print('As raizes da equação são: ', raiz1, 'e', raiz2)


x = float(input('Digite o A: '))
y = float(input('Digite o B: '))
z = float(input('Digite o C: '))

bhaskara(x, y, z)
