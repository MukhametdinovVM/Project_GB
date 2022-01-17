from sys import argv

name, time, stavka, bonus = argv

try:
    time = int(time)
    stavka = int(stavka)
    bonus = int(bonus)
    zp = time * stavka + bonus
    print(f'Заработная плата: {zp}')
except ValueError:
    print('Не число')
