status = 'Выполняется'
print(status)

while True:
    # Изменение статуса заметки
    status_change = input('Введите статус заметки в виде "Выполняется"; "Выполнено"; "Отложено": ').lower()
    if status_change == 'выполняется':
        status = ('Выполняется')
        break
    elif status_change == 'выполнено':
        status = 'Выполнено'
        break
    elif status_change == 'отложено':
        status = 'Отложено'
        break
    else:
        print('Некорректное значение, проверьте ввод.')