titles = []
print('Чтобы остановить ввод введите "стоп"')
while True:
    # Цикл ввода заголовков
    title = input('Введите заголовок: ')
    if title.lower() == 'стоп':
        break
    if titles.count(title.lower()):
        answer = input('Такой заголовок уже есть в заметке, добавить повторно? Введите да/нет: ')
        if answer.lower() == 'да':
            pass
        else:
            continue
    titles.append(title.lower())

n = 1
for title in titles:
# Вывод отформатированных заголовков
    if title == '':
        continue
    # Пропуск пустых заголовков
    print(f'Заголовок №{n} - {title.title()}')
    n += 1
