"""
В ООП очень важно предварительное проектирование. В общей сложности можно выделить
следующие этапы разработки объектно-ориентированной программы:
1. Формулирование задачи.
2. Определение объектов, участвующих в ее решении.
3. Проектирование классов, на основе которых будут создаваться объекты. В случае
необходимости установление между классами наследственных связей.
4. Определение ключевых для данной задачи свойств и методов объектов.
5. Создание классов, определение их полей и методов.
6. Создание объектов.
7. Решение задачи путем организации взаимодействия объектов.
"""


class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    # def lose(self):
    #     from random import randrange
    #     if self.knowledge:
    #         i = randrange(len(self.knowledge))
    #         del self.knowledge[i]

    def lose(self):
        import random
        if self.knowledge:
            self.knowledge.remove(random.choice(self.knowledge))


# from test import *
lesson = Data('class', 'object', 'inheritance', 'polymorphism',
              'encapsulation')
pupil = Pupil()
for i in lesson:
    pupil.take(i)

print(pupil.knowledge)

pupil.lose()
print(pupil.knowledge)

pupil.lose()
print(pupil.knowledge)
