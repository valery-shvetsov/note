import interface
import database_module
import logger
import import_from_file as iff
import export_to_file


def run():
    
    while True:
    
        command = interface.start_page()

        match command:
            case '1':     # Список всех заметок
                data = database_module.get_all_note()
                interface.show_note(data)

            case '2': # Поиск заметки
                user_search = interface.search_note()
                data = database_module.get_note_info(user_search)
                interface.show_note(data)
            
            
            case '3': # Добавить заметку

                new_note = interface.add_note()
                database_module.add_note(new_note)
                logger.add(new_note, 'added')
                interface.done_message()

            case '4': # Изменить заметку
                data = database_module.get_all_note()
                interface.show_note(data)
                deal_id = interface.change_note()
                one_note = database_module.get_one_note(deal_id)
                changed_note = interface.change_note_content(one_note)
                if changed_note['note'] == 'Я что-то нажал и всё сломалось':
                    database_module.delete_note(changed_note['note_id'])
                    logger.add(changed_note, 'deleted')
                else:
                    database_module.change_note(changed_note)
                    logger.add(changed_note, 'changed')
            
            case '5': # Импорт
                user_choice = interface.import_note()
                if user_choice == '1':
                    data = iff.import_csv('import_note.csv')
                    database_module.add_note(data)
                    interface.result_mess(True)
                    logger.add(data, 'imported')
                elif user_choice == '2':
                    data = iff.import_json('import_note.json')
                    database_module.add_note(data)
                    interface.result_mess(True)
                    logger.add(data, 'imported')
                else:
                    interface.error_input()
                
                
            
            case '6': # Экспорт
                user_choice = interface.export_note()
                if user_choice == '1':
                    data = export_to_file.export_csv()
                    interface.result_mess(True)
                    #logger.add(data, 'exported')
                elif user_choice == '2':
                    data = export_to_file.export_json()                                    
                    interface.result_mess(True)
                    #logger.add(data, 'exported')
                else:
                    interface.error_input()

            case '7': # Выход
                interface.bye_mess()
                break
            
            case _:
                interface.error_input()


def change_action(user_answer: dict):
    match user_answer['user_choise']:
        case 1: # завершить дело
            return
        
        case 2: # изменить дело
            return

        case 3: # удалить дело
            return