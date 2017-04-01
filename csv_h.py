import csv

answers= { 

        'Привет': 'И тебе привет!',
        'Как дела?': 'Лучше всех', 
        'Пока': 'Увидимся' 

        }

with open('export.csv', 'w', encoding = 'utf-8') as f:
    fields = ['key', 'value']
    writer = csv.DictWriter(f, fields, delimeter = ':')
    writer.writeheader()
    for questions in answers:
        writer.writerow(questions)