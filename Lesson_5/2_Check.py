my_file = open('test.txt', "r")

a = 1

for line in my_file:
    words = len(line.split())
    # print(words)
    symbols = len(line)
    # print(symbols)
    print(f"В {a} строке {words} слов(о/а) - {symbols} символ(а/ов)")
    a += 1

my_file.close()
