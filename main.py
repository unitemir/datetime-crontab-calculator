from datetime import datetime, timedelta


def next_start(start_date, crontab):
    mins, hours, wdays, days, months = [list(map(int, part.split(','))) for part in crontab.rstrip(';').split(';')]


    current_date = start_date

    while True:
        if current_date.month in months:
            if current_date.day in days:
                if (current_date.weekday() + 1) % 7 in wdays:  # +1 и % 7 для соответствия американскому календарю
                    for hour in sorted(hours):
                        if hour >= current_date.hour:
                            for minute in sorted(mins):
                                if (hour == current_date.hour and minute > current_date.minute) or (hour > current_date.hour):
                                    return datetime(current_date.year, current_date.month, current_date.day, hour, minute)
            current_date = datetime(current_date.year, current_date.month, current_date.day) + timedelta(days=1)
            current_date = current_date.replace(hour=0, minute=0)  # Сбрасываем часы и минуты
        else:
            if current_date.month == 12:
                current_date = datetime(current_date.year + 1, 1, 1)
            else:
                current_date = datetime(current_date.year, current_date.month + 1, 1)
            current_date = current_date.replace(hour=0, minute=0)


start_date = datetime(2010, 7, 9, 23, 36)
crontab = "0,45;12;1,2,6;3,6,14,18,21,24,28;1,2,3,4,5,6,7,8,9,10,11,12;"
print(next_start(start_date, crontab))
