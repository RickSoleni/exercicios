try:  # tentar abrir o arquivo 1
    fin = open('words.txt')
except:
    print('Arquivo não encontrado')
    exit()


def sed(
    string1, stringsubst, file1, file2
):  # função para ler e copiar arquivo 1 e colar no arquivo 2
    for line in file1:
        if line.strip() == string1.lower():
            line = line.replace(string1, stringsubst)
        file2.write(line)


try:  # tentar chamar a função sed
    fout = open('novoarquivo.txt', 'w')
    sed('gone', 'ABUBLE', fin, fout)
except:
    print('Não é possível ler ou alterar o arquivo')

try:  # tentar fechar o programa

    fout.close()
except:
    print('Não é possível fechar/salvar o arquivo')
