from datetime import datetime
import csv
import random

user_ids = [1, 2, 3, 4, 5]
websystem = [1, 2, 3]
times = [i for i in range(1, 30)]
traffics = [i for i in range(1, 50)]
dates = [f'2023/12/{str(i)}' for i in range(10, 22)]

with open('../media/data.csv', 'w+', encoding='UTF-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Дата', 'Время', 'Трафик', 'Пользователь', 'Вэб-система'])
    for i in range(50):
        date = random.choice(dates)
        writer.writerow([datetime.strptime(date, '%Y/%m/%d'),
                         random.choice(times),
                         random.choice(traffics),
                         random.choice(user_ids),
                         random.choice(websystem),
                         ])
