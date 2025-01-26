notes = [{'username': 'Антон', 'title': 'Покупки', 'content': 'Купить еду'},
        {'username': 'Анна', 'title': 'Стоматолог', 'content': 'Сходить к стоматологу'}
        ]

# Для отформатированного выведения заметок в этом файле, в итоговом проекте использоваться не будет
def show_form_note(list):
    n = 1
    for note in list:
        print(f'\nЗаметка №{n}')
        for key,value in note.items():
            print(f'\t{key.title()}: {value}')
        n += 1

show_form_note(notes)

def delete_note():
    filtered_list = []
    name = input('Введите имя пользователя: ')
    for note in notes:
        if name not in note.values():
            filtered_list.append(note)
    return filtered_list


while True:
    if notes:
        if input('Хотите удалить заметку? да/нет ') == 'да':
            filtered_list = delete_note()
        else:
            break

try:
    show_form_note(filtered_list)
except:
    pass
