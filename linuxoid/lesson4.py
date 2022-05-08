"""
    Наследование в ООП – это скорее аналог систематизации и классификации наподобие той,
    что есть в живой природе. Все млекопитающие имеют четырехкамерное сердце, но только
    носороги – рог.
"""


# Простое наследование методов родительского класса
class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


class DeskTable(Table):
    def square(self):
        return self.width * self.length


t1 = Table(1.5, 1.8, 0.75)
t2 = DeskTable(0.8, 0.6, 0.7)
print(t2.square())  # вывод: 0.48


# Полное переопределение метода надкласса
class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


class DeskTable(Table):
    def square(self):
        return self.width * self.length


class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.width * self.length - monitor


t3 = ComputerTable(0.8, 0.6, 0.7)
print(t3.square(0.3))  # вывод: 0.18


# Дополнение, оно же расширение, метода
# wrong method
class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.length


class KitchenTable(Table):
    def __init__(self, length, width, height, places):
        self.length = length
        self.width = width
        self.height = height
        self.places = places


t4 = KitchenTable(1.5, 2.5, 0.75, 6)
print(t4.square())


# true method
class Table:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.length


class KitchenTable(Table):
    def __init__(self, length, width, height, places):
        super().__init__(length, width, height)
        self.places = places


t5 = KitchenTable(1.5, 3.1, 0.75, 6)
print(t5.square())

# Параметры со значениями по умолчанию у родительского класса
