'''Переведите содержимое файла purchase_log.txt в словарь purchases вида:
{'1840e0b9d4': 'Продукты', ...}
 '''

import json

purchases = {}

with open(r'C:\Users\79090\OneDrive\Рабочий стол\Учеба\Python для инженерии данных\Работа с файлами и пакетами\Материалы к ДЗ 1\purchase_log.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        if i == 0:
            continue
        line = line.strip()
        dict_ = json.loads(line)
        purchases[dict_.get('user_id', None)] = dict_.get('category', None)
        #if i > 3:
            #break
print(purchases)

