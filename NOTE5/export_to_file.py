from database_module import get_all_note
import csv
import json

def export_csv():
    temp = get_all_note() # Возвращает весь справочник из рабочего файла

    file_csv = "bd_csv_export.csv" # задали имя файлу в который выгружаем

    with open(file_csv,"w", encoding='UTF-8', newline="") as file: 
        colone = temp[0].keys()
        writer = csv.DictWriter(file, fieldnames=colone)
        writer.writeheader()
        writer.writerows(temp)
    
    print(f"данные перенесены в файл {file_csv}")

    return 

def export_json():
    temp = get_all_note() # Возвращает весь справочник из рабочего файла

    file_json = "bd_json_export.json" # задали имя файлу в который выгружаем

    with open(file_json,"w", encoding='UTF-8', newline="") as file: 
        writer = json.dump(temp,file)
#        writer.writeheader()
#        writer.writerows(temp)
    
    print(f"данные перенесены в файл {file_json}")

    return 