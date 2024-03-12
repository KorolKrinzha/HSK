import csv
import json

def csv_to_json(csv_file, json_file):
    data = {}
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок

        # Проходимся по каждой строке, собирая о словах
        for row in reader:
            """
            Файлы CSV устроены следующим образом
            Слово,Транскрипция,Перевод
            """
            word = row[0]
            transcription = row[1]
            translation = row[2]

            # записываем новое слово
            data[word] = {'translation': translation,
                          'transcription': transcription}

    # заполненный словарь записываем в json
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

"""
всего проходимся по четырем файлам, 
так как у нас в боте изучаются четыре экзамена 
"""
for i in range(1, 4+1):
    csv_to_json(f"CSV\HSK{i}.csv", f"HSK{i}.json")
