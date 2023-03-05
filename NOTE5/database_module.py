import json

path_to_db = 'db_note.json'

def get_all_note():  # Возвращает весь список заметок из файла db_phonebook.json
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data = [data[i] for i in range(0, len(data))]
    return data

def get_one_note(note_id_get): # Возвращает одну заметку по его note_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        one_note_get = {}
        for i in range(0, len(data)): 
            if note_id_get == data[i]['note_id']:
                one_note_get = data[i]
                break
    return one_note_get

def get_note_info(note_info_get): # Возвращает заметки по вхождению в значение любого из ключей surname, name, phone, comment
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
        info_note_get = []

        for i in range(0, len(data)): 
            if  note_info_get.lower() in data[i]['title'].lower():
                info_note_get.append(data[i])
            elif note_info_get.lower() in data[i]['creation_date'].lower():
                info_note_get.append(data[i])
            elif note_info_get.lower() in data[i]['importance'].lower():
                info_note_get.append(data[i])
            elif note_info_get.lower() in data[i]['note'].lower():
                info_note_get.append(data[i])
 
    return info_note_get

def add_note(note_new_dict):  # Добавление новых заметок в БД 
                #[{'note_id': ', 'title': 'учеба', 'creation_date': '2023-02-04 20:15', 'importance': 'важно.', 'note': 'сдать проект'}, 
                #{'note_id': '', 'title': 'работа', 'creation_date': '2023-02-04 20:15', 'importance': 'не срочно', 'note': 'сделать отчет'}]
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)            
        for i in range(0, len(note_new_dict)): 
            note_new_dict[i]['note_id'] = data[len(data)-1]['note_id'] + 1
            data.append(note_new_dict[i])     # Добавляем в список словарей новый контакт   
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)

def change_note(note_edit):  # Изменение заметки
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)

        for i in range(0, len(data)): # Для изменения заметки c note_id = 6, находим в БД словарь с nout_id = 6 и перезаписываем его.
            if note_edit['note_id'] == data[i]['note_id']:
                data[i] = note_edit
        
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def delete_note(note_id_delete): # Удаление заметки в БД по его note_id
    with open(path_to_db, 'r', encoding='UTF-8') as file: # Читаем данные из базы. 
        data = json.load(file)
                  
        for i in range(0, len(data)): 
            if data[i]['note_id'] == note_id_delete: # находим индекс элемента в списке словарей с нужным deal_id
                index_del = i
                break
        data.pop(index_del)   # Удаляем из списка словарь с нужным note_id
        for i in range(0, len(data)): # Перезаписаваем в каждом словаре списка ключ note_id
            data[i]['note_id'] = i+1
    with open(path_to_db, 'w', encoding='UTF-8') as file: # Записываем в базу данных обновленный список словарей
        json.dump(data, file, indent=4)    

def clear_db(path_to_db): # Очистка базы данных
    first_element = [{'note_id': 0}, ]
    with open(path_to_db, 'w') as file:
        json.dump(first_element, file, indent=4)

#if __name__ == "__main__":
#Тестирование БД на тестовых данных test_data
    # from pprint import pprint
    
    # path_to_db = 'test_db_note.json'
    
    # clear_db(path_to_db)
    # test_data =[{'note_id': 1, 'title': 'Иванов', 'creation_date': 'Иван', 'importance': '111', 'note': 'Друг'}, 
    #             {'note_id': 2, 'title': 'Петров', 'creation_date': 'Петр', 'importance': '222', 'note': 'Коллега'},
    #             {'note_id': 3, 'title': 'Сидоров', 'creation_date': 'Сидор', 'importance': '333', 'note': 'Должен 1000'},
    #             {'note_id': 4, 'title': 'Ромашкина', 'creation_date': 'Маша', 'importance': '444', 'note': 'Вкусные пирожки'},
    #             {'note_id': 5, 'title': 'Василькова', 'creation_date': 'Оля', 'importance': '555', 'note': 'Большие глаза'}]
    

    # with open (path_to_db, 'w') as test_file:
    #     json.dump(test_data,test_file, indent=4)

    # print('')
    # print('***get_all_note()***')
    # pprint(get_all_note(), sort_dicts=False)

    # print('')
    # print('***add_note(test_note_add)***')
    # test_note_add = [{'note_id': '', 'title': 'Петров', 'creation_date': 'Иван', 'importance': '111', 'note': 'Друг'}, 
    #                     {'note_id': '', 'title': 'Васильков', 'creation_date': 'Иван', 'importance': '111', 'note': 'Друг'}]
    # print('***')
    # print(test_note_add)    
    # print('***')    
    # add_note(test_note_add)
    # with open (path_to_db, 'r') as test_file:
    #     text = json.load(test_file)
    #     pprint(text, sort_dicts=False)

    # print('')
    # print('***change_note(test_note_edit)***')
    # test_note_edit = {'note_id': 3, 'title': 'Сидоров', 'creation_date': 'Сидор', 'importance': '333', 'note': 'Должен 7777000'}
    # change_note(test_note_edit)
    # with open (path_to_db, 'r') as test_file:
    #     text = json.load(test_file)
    #     pprint(text, sort_dicts=False)

    # print('')
    # print('***get_one_note(test_note_id_get)***')
    # test_note_id_get = 3
    # print(get_one_note(test_note_id_get))

    # print('')
    # print('***delete_note(note_delete)***')
    # test_note_id_delete = 5
    # print('***')
    # print(get_one_note(test_note_id_delete))
    # print('***')
    # delete_note(test_note_id_delete)
    # with open (path_to_db, 'r') as test_file:
    #     text = json.load(test_file)
    #     pprint(text, sort_dicts=False)
        
    # print('')
    # print('***get_note_info(note_info_get)***')
    # print('***')
    # note_info_get = 'дол'
    # print(note_info_get)
    # print('***')
    # pprint(get_note_info(note_info_get), sort_dicts=False)