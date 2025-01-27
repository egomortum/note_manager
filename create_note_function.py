from _datetime import datetime
notes = []

def make_note():
    note = {
        'username': input('Введите имя пользователя: '),
        'titles': input('Введите заголовок заметки: '),
        'content': input('Введите содержание заметки: '),
        'status': input('Введите статус заметки (новая, в процессе, выполнено): '),
        'created_date': datetime.now(),
        'issue_date': datetime.strptime(input('Введите дату дедлайна в формате гг-мм-дд: '), '%Y-%m-%d')
    }
    notes.append(note)

make_note()
print(notes)