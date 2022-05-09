# class Rectangle:
#     def __init__(self, width, height, sign):
#         self.w = int(width)
#         self.h = int(height)
#         self.s = str(sign)
#
#     def __str__(self):
#         rect = []
#         for i in range(self.h):
#             rect.append(self.s * self.w)
#         rect = '\n'.join(rect)
#         return rect
#
#     def __add__(self, other):
#         return Rectangle(self.w + other.w, self.h + other.h, self.s)
#
#
# a = Rectangle(4, 2, 'w')
# print(a)
# b = Rectangle(8, 3, 'y')
# print(b)
# print(a + b)
# print(b + a)

from random import randint


class Animal:
    def __init__(self, a, b):
        self.prop1 = a
        self.prop2 = b

    def __add__(self, other):
        n = randint(1, 2)
        if n == 1:
            return Animal(self.prop1, other.prop2)
        else:
            return Animal(other.prop1, self.prop2)

    def __str__(self):
        return f'{self.prop2} {self.prop1}'


unit1 = Animal('cat', 'black')
unit2 = Animal('cat', 'white')
unit3 = unit1 + unit2
print(unit3)
