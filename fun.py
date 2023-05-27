import re
import gspread
import json

gs = gspread.service_account(filename='botvvsu-aab43c686f18.json')   # подключаем файл с ключами и пр.
sh = gs.open_by_key('1e2o-5Mu7aIJMNGIu-C-qzHk-opGFmAIdWZ3lKOlpQLY')  # подключаем таблицу по ID
sheets_name = sh.worksheets()


subjects = []
for sheet in sheets_name:
    if re.search(r'(\S)+[-]+(\d{2})', sheet.title):                                                                                                 # формируем список списков по названиям групп
        for sheet_value in sheet.get_all_values():
            if (sheet_value[0] != 'ДИСЦИПЛИНА') and ('Учебный год' not in sheet_value[0]) and not re.search(r'(\S)+[-]+(\d{2})', sheet_value[0]):   # Сравнивать строку с названием Sheet
                subjects.append(sheet_value[0].strip())
subjects = sorted(list(set(subjects)))

subjects_dict = {i+1 : subjects[i] for i in range(len(subjects))}


callback_dict = {i+1 : {
                          'title': subjects[i],
                          'status': False,
                          'cost': None,
                          'schedule': None,
                          'room': None,
                          'teacher': None,
                          'comment': None
                       }
                                                for i in range(len(subjects))}



# def write(data, filename):
#     data = json.dumps(data)
#     data = json.loads(str(data))
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, indent=4, ensure_ascii=False)
# write(callback_dict, 'data.json')







