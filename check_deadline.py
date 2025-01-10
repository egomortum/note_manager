from _datetime import datetime

def get_current_date():
    # Получение сегодняшней даты
    current_date = datetime.now()
    return current_date

def get_issue_date():
    # Получение даты дедлайна
    msg = 'Введите число в формате год-месяц-день: '
    while True:
        try:
            issue_date = datetime.strptime(input(msg), '%Y-%m-%d')
            return issue_date
        except ValueError:
            print('Проверьте ввод.')
            continue

def check_deadline():
    # Проверяет состояние дедлайна
    cur_date = get_current_date()
    iss_date = get_issue_date()
    if cur_date > iss_date:
        a = cur_date - iss_date
        print(f'Дедлайн просрочен на {a}')
    elif cur_date < iss_date:
        a = iss_date - cur_date
        print(f'До дедлайна ещё {a}')
    else:
        print('Дедлайн сегодня.')

print(f'Сейчас: {get_current_date()}')
check_deadline()
