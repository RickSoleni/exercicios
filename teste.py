import random

dic = {'Pedro': 99, 'João': 19, 'Rosa': 35, 'Maria': 23}
name, id = random.choice(list(dic.items()))

print(name, id)
