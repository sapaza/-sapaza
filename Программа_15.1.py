p = "ключ1,ключ2,ключ3,ключ4,ключ5"
keys = p.split(',')
if keys:
    number = keys.index('ключ3')
    if number:
        print(f'Ключ 3 найден! Индекс: {number}')
    else:
        print('Ошибка :(')
    places = ['пещера', 'лес', 'река', 'гора', 'болото']
    sort_pl = sorted(places)
    print(f'Отсортированные места: {sort_pl}')
    numeral = sort_pl.index('лес')
    print(f'Созданный код: {numeral}-{sort_pl[numeral]}')
    code = f'{numeral}-{sort_pl[numeral]}'
    if code == '2-лес':
        print('Сундук открыт!')
    else:
        print('Ошибка :(')