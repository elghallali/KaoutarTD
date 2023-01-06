class Date:
    months = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']

    def __init__(self, day, month, year):
        if not self.is_valid_date(day, month, year):
            raise ValueError('Date impossible')
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.day} {self.months[self.month-1]} {self.year}"

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.day < other.day
        return False

    def is_valid_date(self, day, month, year):
        if month == 2:
            if year % 4 == 0:
                return  1 <= day <= 29 and year > 1900
            else:
                return  1 <= day <= 28 and year > 1900
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= day <= 31 and year > 1900
        elif month in [4, 6, 9, 11]:
            return 1 <= day <= 30 and year > 1900
        else:
            return False


d1 = Date(30, 1, 1989)
d2 = Date(3, 1, 1989)

print(d1 < d2)  # Affiche: True
print(d2 < d1)  # Affiche: False