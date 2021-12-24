time_second = int(input('Введите время в секундах: '))

time_hour = time_second//3600
time_minute = time_second%3600//60
time_second = time_second%3600%60

if time_hour < 10:
    time_hour = '0'+ str(time_hour)
if time_minute < 10:
    time_minute = '0'+ str(time_minute)
if time_second < 10:
    time_second = '0'+ str(time_second)

print(f'{time_hour}:{time_minute}:{time_second}')