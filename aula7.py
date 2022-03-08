def has_duplicates(lista):
    lista = sorted(lista)
    for item in range(len(lista) - 1):
        if lista[item] == lista[item + 1]:
            return True
    return False


a = [1, 3, 4, 3]
print(has_duplicates(a))
