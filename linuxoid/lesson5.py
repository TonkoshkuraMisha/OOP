"""
    Полиморфизм в объектно-ориентированном программировании – это возможность обработки
разных типов данных, т. е. принадлежащих к разным классам, с помощью "одной и той же"
функции, или метода. На самом деле одинаковым является только имя метода, его исходный код
зависит от класса. Кроме того, результаты работы одноименных методов могут существенно
различаться. Поэтому в данном контексте под полиморфизмом понимается множество форм
одного и того же слова – имени метода.
Например, два разных класса содержат метод total, однако инструкции каждого
предусматривают совершенно разные операции. Так в классе T1 – это прибавление 10 к
аргументу, в T2 – подсчет длины строки символов. В зависимости от того, к объекту какого
класса применяется метод total, выполняются те или иные инструкции.
"""


class T1:
    def __init__(self):
        self.n = 10

    def total(self, a):
        return self.n + int(a)


class T2:
    def __init__(self):
        self.string = 'Hi'

    def total(self, a):
        return len(self.string + str(a))


t1 = T1()
t2 = T2()
print(t1.total(35))  # Вывод: 45
print(t2.total(35))  # Вывод: 4


class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2


a = A(3, 4)
b = str(a)
print(a)
print(b)


class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

    def __str__(self):
        s = str(self.field1) + " " + str(self.field2)
        return s


a = A(3, 4)
b = str(a)
print(a)
print(b)


class Rectangle:
    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)

    def __str__(self):
        rect = []
        # количество строк
        for i in range(self.h):
            # знак повторяется w раз
            rect.append(self.s * self.w)
            # превращаем список в строку
        rect = '\n'.join(rect)
        return rect


b = Rectangle(10, 3, '*')
print(b)
