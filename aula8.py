fin = open('words.txt')

dicionario = {}
for line in fin:
    word = line.strip()
    dicionario[word] = ''


def verificastring(palavra, dicion):
    if palavra in dicion:
        return True
    return False


# print(dicionario)

a = 'banana'

b = verificastring(a, dicionario)
print(b)
