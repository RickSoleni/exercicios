fin = open('words.txt')


def uses_all(palavra: str, allowlist: list[str]) -> bool:
    for letra in allowlist:
        if palavra.find(letra) == -1:
            return False
    return True


listaletras = ['a', 'c', 'e', 'f', 'h', 'l', 'o']
contagem = 0
for line in fin:
    palavra = line.strip()
    if uses_all(palavra, listaletras):
        contagem += 1
print('Numero de palavras com somente essas letras: ', contagem)
