username = input('Введите своё имя: ')
title1 = input('Введите заголовок заметки: ')
title2 = input('Введите заголовок заметки: ')
title3 = input('Введите заголовок заметки: ')
titles = [title1, title2, title3]
content = input('Введите содержание заметки: ')
status = input('Введите статус заметки ')
create_date = input('Введите дату создания заметки в формате: дд.мм.гг ')
issue_date = input('Введите дату истечения действия заметки в формате: дд.мм.гг ')

print(username, titles, content, status, create_date, issue_date, sep='\n')