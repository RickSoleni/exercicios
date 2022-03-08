import datetime

data_atual = datetime.datetime.now()
aniversario = datetime.date(2022, 11, 30)
diasfaltantes = data_atual - aniversario

print(diasfaltantes)
