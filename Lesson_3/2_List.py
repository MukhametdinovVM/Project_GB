name = input('Введите Имя: ')
surname = input('Введите Фамилию: ')
year = int(input('Введите возраст: '))
city = input('Введите город: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

def my_func(name, surname, year, city, email, phone):
     print(f"Фамилия - {surname}; Имя - {name}; Возраст - {year}; Город - {city}; email - {email}; Телефон - {phone}")

print(my_func(name, surname, year, city, email, phone))
