fin = open('words.txt')


def evitou(word: str, letrasproibidas: list[str]) -> bool:
    for letra in letrasproibidas:
        if (
            word.find(letra) != -1
        ):  # se ele achar (diferente de -1: find -1 == não achou) retorna falso
            return False
    return True


inputs = []
while True:
    value = input('Digite uma letra proibida, ou digite 0 para sair: ')
    if value == '0':
        break
    inputs.append(value)

contagem = 0

for line in fin:
    word = line.strip()
    if evitou(word, inputs):
        contagem += 1
print('O numero de palavras sem as letras é: ', contagem)
