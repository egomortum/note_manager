notes = []

def make_note():
    while True:
        username = input('Введите имя пользователя: ')
        titles = []
        print('Чтобы завершить введение заголовков введите "q"')
        while True:
            title = input('Заголовок: ')
            if title == 'q':
                break
            titles.append(title)
        content = input('Содержание: ')
        status = input('Статус заметки: ')
        created_date = input('Дата создания в формате дд-мм-гг: ')
        issue_date = input('Дата дедлайна в формате дд-мм-гг: ')
        note = {'username': username,
                'titles': titles,
                'content': content,
                'status': status,
                'created date': created_date,
                'issue date': issue_date
        }
        return note

def add_note_in_list():
    while True:
        d = input('Хотите добавить ещё одну заметку? yes/no ')
        if d == 'no':
            break
        notes.append(make_note())

def show_formatted_notes():
    for note in notes:
        for key,value in note.items():
            if key == 'titles':
                n = 1
                for title in value:
                    print(f'Заголовок №{n}: {title}')
                    n += 1
                continue
            print(f'{key.title()}: {value}')

add_note_in_list()
show_formatted_notes()