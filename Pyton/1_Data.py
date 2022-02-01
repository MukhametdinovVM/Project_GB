class DataClass:

    def __init__(self, date):
        self.date = date

    @classmethod
    def m_1(cls, date):
        my_date = []
        for i in date.split("-"):
            my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def m_2(d, m, y):
        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 0 < y <= 2022:
                    return f"Дата указана верно!!!"
                else:
                    return f"Год указан неверно!"
            else:
                return f"Месяц указан неверно!"
        else:
            return f"День указан неверно!"

    def __str__(self):
        return f"Вы указали дату {Data_Class.m_1(self.date)}"


data = DataClass("10-06-1989")
print(data)
print(DataClass.m_2(32, 6, 1989))
print(DataClass.m_2(10, 6, 2023))
print(DataClass.m_1("10-06-1989"))