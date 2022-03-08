def invert_dict(dicionario):
    invert = dict()
    for key in dicionario:
        valor = dicionario[key]
        invert.setdefault(valor, key)
    return invert


a = {'model': 'Ford', 'year': 1964, 'portas': 'duas portas'}

b = invert_dict(a)
print(b)

"""def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse"""
