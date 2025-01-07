d = []
y = 0
d.append('Пойти в лицей')
d.append('Сходить в бассейн')
d.append('Пропылесосить')
d.append('Полить цветы')
d.append('Покормить кота')
d.append('Изучать списки')
i=0
print("Записи:")
for i in range (6):
    print(d[i])
    i = i+1
print('\n')
d[5] = 'Понять списки!'
d.append ('Прочитать книгу')
del d[0]
j = 0
print("Обновлённые записи:")
for j in range (6):
    print(d[j])
    j = j +1