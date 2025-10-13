def in_minutes(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return [mins, secs]
seconds = int(input('Введите количество секунд:'))
mins, secs = in_minutes(seconds)
print(f"{mins} минут, {secs} секунд")