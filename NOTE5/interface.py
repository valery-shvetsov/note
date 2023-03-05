# Необходимо написать проект, содержащий функционал работы с заметками. 
# Программа должна уметь: 
# создавать заметку, 
# сохранять её, 
# читать список заметок, 
# редактировать заметку, 
# удалять заметку.
# делать выборку по дате

import datetime
import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

def error_input():
    print('\033[5;31mОшибка!')
    print('\033[0m\033[21mПожалуйста введите команду соответствующую пункту меню.\033[0m')
    time.sleep(1)


def done_message():
    print('\033[5;32mВыполнено!')

main_menu = \
    'Выберите пункт меню:\n\
    1. \033[4mСписок заметок\033[0m\n\
    2. \033[4mПоиск заметки\033[0m\n\
    3. \033[4mДобавить заметку\033[0m\n\
    4. \033[4mИзменить или удалить заметку\033[0m\n\
    5. \033[4mИмпорт заметки\033[0m\n\
    6. \033[4mЭкспорт заметки\033[0m\n\
    7. \033[4mВыход\033[0m'

def start_page():  # Starting page, choose number
    print(main_menu)
    print()
    command = input('\033[1mВыберите действие: \033[0m')
    print(50 * "_")
    return command

def show_note(data):  # 1 in menu

    if data != []:
        print('\033[4mСписок заметок:\033[0m')
        for item in range(len(data)):
            a = data[item]['note_id']
            b = data[item]['title']
            c = data[item]['creation_date']
            d = data[item]['importance']
            e = data[item]['note']
#            print(f" id {a}. {b} {c}. {d}. {e}.")
            print(f"ID {a}. {b}. {c}. {d}. {e}.")
        print(50 * "•")
    else:
        print('\033[33mСписок заметок пуст\033[0m')

def search_note():
    print('Поиск производится по всем полям')
    print('Для точного поиска заметки по дате введите ее в формате YYYY-MM-DD HH:mm')
    search_request = input('Введите данные для поиска: ')
    print(50 * "=")
    return search_request

def add_note():
    print('\033[3mДобавление заметки\033[0m')
    print(50 * "-")
    print(Fore.GREEN)
    title = input('Введите название: ')  # plain text
    print(Fore.YELLOW)
    #creation_date = input('Введите дату создания: ')  # 
    creation_date = datetime.datetime.now()
    creation_date = creation_date.strftime("%Y-%m-%d %H:%M")
    print(f"Дата создания заметки' {creation_date}")
    print(Fore.CYAN)
    importance = input('Введите степень важности: ')
    print(Fore.MAGENTA)
    note = input('Введите заметку: ')
    print(Style.RESET_ALL)
    contact = [{'note_id': '', 'title': title, 'creation_date': creation_date, 'importance': importance,
                'note': note}, ]
#    contact = [{'note_id': '', 'title': contact_surname, 'creation_date': contact_name, 'importance': contact_number,
#                'note': commentary}, ]
    return contact  # возвращение списка словаря



def change_note():
    print('\033[4mИзменить заметку:\033[0m')
    print(50 * "~")
    note_id = input('Введите ID заметки для внесения изменений: ')
    return int(note_id)

def change_note_content(one_contact):
    while True:
        menu_command = input('Что необходимо сделать?\n 1 - Изменить поля заметки \n 2 - Удалить заметку\n')
        if menu_command == '1':
            print('\033[4mИзменить поля заметки:\033[0m')
            while True:
                submenu_command = input(
                    'Что необходимо изменить?\n 1 - Изменить название \n 2 - Изменить дату\n 3 - Изменить степень важности\n 4 - Изменить текст заметки\n')
                match submenu_command:
                    case '1':  # Изменить название
                        print(f"Старое название: {one_contact['title']}")
                        print('Введите новое название: ')
                        one_contact['title'] = input()
                        done_message()
                        break
                    case '2':  # Изменить дату создания
                        print(f"Текущая дата создания: {one_contact['creation_date']}")
                        print('Введите новую дату создания в формате YYYY-MM-DD HH:mm: ')
                        one_contact['creation_date'] = input()
                        done_message()
                        break
                    case '3':  # Изменить степень важности
                        print(f"Старая степень важности: {one_contact['importance']}")
                        print('Введите новую степень важности: ')
                        one_contact['importance'] = input()
                        done_message()
                        break
                    case '4':  # Изменить заметку
                        print(f"Старый текст заметки: {one_contact['note']}")
                        print('Введите новый текст заметки: ')
                        one_contact['note'] = input()
                        done_message()
                        break
                    case _:
                        error_input()
            break
        elif menu_command == '2':
            one_contact['note'] = 'Я что-то нажал и всё сломалось'  # удаление по ID
            done_message()
            break
    return one_contact

def bye_mess():  # 6 in menu
    print('Работа завершена!')

def import_note():
    print('\033[4mИмпорт заметок:\033[0m')
    print('Пожалуйста выберите формат файла для импорта:')
    import_type = input('1-csv\n2-json\n ')
    return import_type

def export_note():
    print('\033[4mЭкспорт заметок:\033[0m')
    print('Пожалуйста выберите формат файла для экпорта:')
    export_type = input('1-csv\n2-json\n')
    return export_type

def result_mess(done):
    if done:
        done_message()
    else:
        print('\033[5;31mПроизошла ошибка при выполнении операции!')

