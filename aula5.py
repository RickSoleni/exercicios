fin = open('words.txt')


def uses_only(palavra: str, allowlist: list[str]) -> bool:
    for letra in palavra:
        if letra not in allowlist:
            return False
    return True


listaletras = ['a', 'c', 'e', 'f', 'h', 'l', 'o']
contagem = 0
for line in fin:
    palavra = line.strip()
    if uses_only(palavra, listaletras):
        contagem += 1
print('Numero de palavras com somente essas letras: ', contagem)
