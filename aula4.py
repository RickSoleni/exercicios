fin = open('words.txt')


def has_no_e(word):
    if word.find('e') == -1:
        return True
    return False


countline = 0
countword = 0

for line in fin:
    word = line.strip()
    countline += 1
    if has_no_e(line):
        print(line)
        countword += 1

print(
    'A porcentagem de palavras sem E é igual a: ',
    countword * 100 / countline,
    '%',
)
