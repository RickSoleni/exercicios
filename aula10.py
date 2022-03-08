from string import punctuation


fin = open('newwords.txt')  # ABRI O ARQUIVO

total_words = []  # CRIEI UMA VARIAVEL PRA GUARDAR TODAS AS PALAVRAS

for line in fin:  # PRA CADA LINHA NO ARQUIVO
    words = line.split(' ')  # CRIO UM ARRAY QUE SEPARA AS PALAVRAS POR ESPAÇO
    special_char = (
        dict()
    )  # CRIO UM DICIONARIO VAZIO PRA GUARDAR OS CARACTERES ESPECIAIS
    for (
        char
    ) in punctuation:  # PRA CADA CARACTER ESPECIAL DENTRO DAS PONTUAÇÕES:
        special_char[
            ord(char)
        ] = None  # CRIO UMA ENTRADA NO DICIONARIO DE CARACTERES ESPECIAIS
    for index, word in enumerate(
        words
    ):  # PRA CADA PALAVRA DENTRO DAS LISTAS DE PALAVRAS
        words[index] = (
            word.strip().lower().translate(special_char)
        )  # APLICOS OS METODOS PARA TIRAR ESPAÇO, DEIXAR MINUSCULO, E REMOVER PONTUAÇÃO USANDO O TRANSLATE
        total_words.append(
            words[index]
        )  # APÓS ISSO ADICIONO ESSA PALAVRA TRATADA DENTRO DO MEU ARRAY DE PALAVRAS TOTAIS

print(
    '\n'.join(total_words)
)  # AQUI USO O \N PRA DAR JOIN, OU SEJA, TODAS AS POSIÇÕES DE ARRAY SERÃO JUNTADAS COM UM \N

# EXEMPLO :

# ['RIC', 'RAFA', 'JOELVALDO']

# '\n'.join(['RIC', 'RAFA', 'JOELVALDO'])

# == 'ric\nrafa\njoelvaldo'

# \n = nextline
