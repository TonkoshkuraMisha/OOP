"""
        В Python наличие пар знаков подчеркивания спереди и сзади в имени метода говорит о том,
    что он принадлежит к группе методов перегрузки операторов (магические методы). Если подобные
    методы определены в классе, то объекты могут участвовать в таких операциях как сложение,
    вычитание, вызываться как функции и др.
"""


class Person:
    def __init__(self, n, s):
        self.name = n
        self.surname = s


p1 = Person("Sam", "Baker")
print(p1.name, p1.surname)


class Rectangle:
    def __init__(self, w=0.5, h=1):
        self.width = w
        self.height = h

    def square(self):
        return self.width * self.height


rec1 = Rectangle(5, 2)
rec2 = Rectangle()
rec3 = Rectangle(3)
rec4 = Rectangle(h=4)
print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec4.square())
