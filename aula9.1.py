def most_frequent(word):
    freq = dict()
    for item in word:
        if freq.get(item):
            freq[item] += 1
        else:
            freq[item] = 1
    for i in sorted(freq, key=freq.get, reverse=True):
        print(i, freq[i])


palavra = 'rafael'
print(most_frequent(palavra))
