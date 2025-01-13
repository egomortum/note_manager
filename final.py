username = input('Введите своё имя: ')
title1 = input('Введите заголовок заметки: ')
title2 = input('Введите заголовок заметки: ')
title3 = input('Введите заголовок заметки: ')
titles = [title1, title2, title3]
content = input('Введите содержание заметки: ')
status = input('Введите статус заметки ')
create_date = input('Введите дату создания заметки в формате: дд.мм.гг ')
issue_date = input('Введите дату истечения действия заметки в формате: дд.мм.гг ')

note = [
    username,
    titles,
    content,
    status,
    create_date,
    issue_date
]

def show_titles():
    print("Заголовки: ")
    for title in titles:
        print(f'\t {title}')

print(f'Имя пользвателя: {note[0]}')
show_titles()
print(f'Содержание: {note[2]}')
print(f'Статус: {note[3]}')
print(f'Дата создания: {note[4]}')
print(f'Дата дедлайна: {note[5]}')
