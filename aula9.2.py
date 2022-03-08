def anagram_on_file(filename: str) -> dict:
    fin = open(filename)  # file in -> fin
    anagrams = dict()  # criei um dicionario
    for item in fin:  # pra cada linha dentro do arquivo
        word = item.strip()  # separei as palavras (tirei espaços)
        sorted_word = ''.join(
            sorted(word)
        )  # ordenei as letras das palavras e juntei pra virar string dnv
        if anagrams.get(
            sorted_word
        ):  # se existir essas letras ordenadas dentro do dicionario
            anagrams[sorted_word].append(
                word
            )  # adiciono essa palavra à lista de palavras com as mesmas letras
        else:  # se não, quer dizer q ainda não existe nenhuma palavra com essas letras no dicionario
            anagrams[sorted_word] = [
                word
            ]  # aí vou lá e adiciono essa palavra na chave dela ordenada

    for key in anagrams:  # pra cada chave dentro dos anagramas
        if (
            len(anagrams[key]) > 1
        ):  # se essa chave for maior que 1, ou seja, se existirem mais de uma palavra com as mesmas letras
            print(anagrams[key])  # printo essa lista de anagramas


anagram_on_file('words.txt')
