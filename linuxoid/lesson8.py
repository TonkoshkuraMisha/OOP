"""
Возможность перегрузки операторов обеспечивает схожесть пользовательского класса со
встроенными классами Python. Ведь все встроенные типы данных Питона – это классы. В
результате все объекты могут иметь одинаковые интерфейсы.
"""


class A:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return str(self.arg)


class B:
    def __init__(self, *args):
        self.aList = []
        for i in args:
            self.aList.append(A(i))

    def __getitem__(self, i):
        return self.aList[i]


group = B(5, 10, 'abc')
print(group.aList[1])  # выведет 10
print(group[0])  # 5
print(group[2])  # abc


class Changeable:
    def __init__(self, color):
        self.color = color

    def __call__(self, newcolor):
        self.color = newcolor

    def __str__(self):
        return "%s" % self.color


canvas = Changeable("green")
frame = Changeable("blue")
canvas("red")
frame("yellow")
print(canvas, frame)
