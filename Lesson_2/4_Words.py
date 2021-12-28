words = list(input('Введите слова чере пробел: ').split())

print(words)

for k, i in enumerate(words, 1):
    if len(i) >= 10:
        i = i[0:10:1]
    print(f'{k}) {i}')
