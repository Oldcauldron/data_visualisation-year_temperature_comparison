
import csv
from datetime import datetime
import io


def reprint(file):  # забирает данные дат и температур из файла
    with io.open(file, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        next(reader)
        highs, dates = [], []
        for r in reader:
            date = datetime.strptime(r[0], '%d.%m.%Y %H:%M')
            if date not in dates:
                dates.append(date)
                try:
                    if r[1]:
                        high = float(r[1])
                    elif r[1] == '' or r[1] is None:
                        raise ValueError
                except ValueError:
                    if highs[-1]:
                        high = float(highs[-1])
                    else:
                        highs[-1] = highs[-2]
                        high = float(highs[-1])
                    highs.append(high)
                else:
                    highs.append(high)
            else:
                continue
        return dates, highs


def days_generator():  # генерирует файл с образцовыми датами за год
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    dates_temple = []
    open('all_dates_2.txt', 'w').close()
    with open('all_dates_2.txt', 'a', encoding='utf-8') as f:
        for a in range(1, 13):
            if a in day_31:
                days = 31
            elif a in day_30:
                days = 30
            elif a == 2:
                days = 28
            for b in range(1, days + 1):
                for c in range(0, 22, 3):
                    f.write(f'2013.{a}.{b} {c}:00\n')
    with open('all_dates_2.txt') as f:
        x = f.readlines()
        for i in x:
            date = datetime.strptime(i.strip('\n\t\r'), '%Y.%m.%d %H:%M')
            dates_temple.append(date)
    return dates_temple


def differents(file, file_2):
    # показывает разницу в годах между файлом 1 и файлом 2
    with io.open(file, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        next(reader)
        reader = [i[0] for i in reader]
        with io.open(file_2, encoding='utf-8', errors='ignore') as f_2:
            reader_2 = csv.reader(f_2)
            next(reader_2)
            reader_2 = [i[0] for i in reader_2]
            resu = list(set(reader) ^ set(reader_2))
            print(f'Result of differents - {file} & {file_2}\n{resu}')
            print('len(set(file) -', len(set(reader)))
            print('len(set(file_2) -', len(set(reader_2)))
            return resu


def reprint_2(file):  # забирает данные дат и температур из файла
    with io.open(file, encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        next(reader)
        date_dic = {}
        before_high = []
        for r in reader:
            try:
                nes_dat = f'2013, {r[6]}, {r[7]}, {r[8]}'
                date = datetime.strptime(nes_dat, '%Y, %m, %d, %H')
            except ValueError:
                continue
            else:
                try:
                    if r[9]:
                        high = float(r[9])
                    elif r[9] == '' or r[9] is None:
                        continue
                except ValueError:
                    continue
                else:
                    if date not in date_dic:
                        date_dic[date] = []
                    date_dic[date].append(high)
                    before_high.append(high)

        return date_dic


