def has_duplicates(lista):
    listanova = dict()
    for item in lista:
        if listanova.get(item, 0):
            return True
        else:
            listanova[item] = 1
    return False


a = [1, 4, 3, 4]
print(has_duplicates(a))
