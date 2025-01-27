from _datetime import datetime

note = {'username': 'Алексей',
        'title': 'Список покупок',
        'content': 'Купить продукты на неделю',
        'status': 'новая',
        'created_date': '27-11-2024',
        'issue_date': '30-11-2024'
}

def update_issue_date():
    while True:
        try:
            issue_date = datetime.strptime(input('Введите дату дедлайна в формате гг-мм-дд: '), '%Y-%m-%d')
            return issue_date
        except:
            print('Некорректный формат даты, проверьте ввод')
            continue

def update_note(note):
    print(note)
    while True:
        key = input('Введите ключ для изменения значения поля: ')
        if key in note.keys():
            if key == 'created_date':
                print('Неизменяемое значение')
                return note
            elif key == 'issue_date':
                note['issue_date'] = update_issue_date()
                return note
            note[key] = input('Введите значение: ')
            return note
        else:
            print('Неверный ключ, проверьте ввод.')
            continue

update_note(note)
print(note)