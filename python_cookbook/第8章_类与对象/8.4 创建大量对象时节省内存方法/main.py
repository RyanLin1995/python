class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Date2:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == '__main__':
    d1 = Date(2022, 3, 4)
    d2 = Date2(2022, 4, 3)
    print(d1.year, d1.month, d1.day)
    print(d2.year, d2.month, d2.day)
