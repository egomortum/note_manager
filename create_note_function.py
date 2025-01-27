from _datetime import datetime
def update_issue_date():
    while True:
        try:
            issue_date = datetime.strptime(input('Введите дату дедлайна в формате гг-мм-дд: '), '%Y-%m-%d')
            return issue_date
        except:
            print('Некорректный формат даты, проверьте ввод')
            continue

def set_status():
    statuses = ['новая','в процессе','выполнено']
    while True:
        try:
            users_choise = int(input('Чтобы выбрать статус заметки из "Новая", "В процессе", "Выполнено" введите 1, 2 или 3 соответственно: '))
            status = statuses[users_choise - 1]
            return status
        except:
            print('Некорректный ввод, попробуйте снова')
            continue


def make_note():
    note = {
        'username': input('Введите имя пользователя: '),
        'titles': input('Введите заголовок заметки: '),
        'content': input('Введите содержание заметки: '),
        'status': set_status(),
        'created_date': datetime.now(),
        'issue_date': update_issue_date()
    }
    return note

print(make_note())