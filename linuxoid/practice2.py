# v 1.0
# from random import randint
#
#
# class Soldier:
#     def make_health(self, value):
#         self.health = value
#
#     @staticmethod
#     def make_kick(enemy):
#         enemy.health -= 20
#
#
# first = Soldier()
# second = Soldier()
# first.make_health(100)
# second.make_health(100)
# while first.health > 0 and second.health > 0:
#     n = randint(1, 2)
#     if n == 1:
#         Soldier.make_kick(second)
#         print("Первый бьет второго")
#         print("У второго осталось", second.health)
#     else:
#         Soldier.make_kick(first)
#         print("Второй бьет первого")
#         print("У первого осталось", first.health)
# if first.health > second.health:
#     print("ПЕРВЫЙ ПОБЕДИЛ")
# elif second.health > first.health:
#     print("ВТОРОЙ ПОБЕДИЛ")

# v 2.0
# from random import randint
#
#
# class Avenger:
#     health = 100
#
#     def set_name(self, name):
#         self.name = name
#
#     def make_kick(self, enemy):
#         enemy.health -= 20
#         print(self.name, "бьет", enemy.name)
#         print('%s = %d' % (enemy.name, enemy.health))
#
#
# first = Avenger()
# second = Avenger()
# first.set_name('Capitan America')
# second.set_name('Iron Man')
# while first.health > 0 and second.health > 0:
#     n = randint(1, 2)
#     if n == 1:
#         first.make_kick(second)
#     else:
#         second.make_kick(first)
# print("ПОБЕДИЛ", end=" ")
# if first.health > second.health:
#     print(first.name)
# elif second.health > first.health:
#     print(second.name)

# v 3.0
from random import randint


class Avenger:
    health = 100

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        enemy.health -= 20
        print(self.name, "бьет", enemy.name)
        print('%s = %d' % (enemy.name, enemy.health))


class Battle:
    result = "Сражения не было"

    def battle(self, u1, u2):
        while u1.health > 0 and u2.health > 0:
            n = randint(1, 2)
            if n == 1:
                u1.make_kick(u2)
            else:
                u2.make_kick(u1)
        if u1.health > u2.health:
            self.result = u1.name + " ПОБЕДИЛ"
        elif u2.health > u1.health:
            self.result = u2.name + " ПОБЕДИЛ"

    def who_win(self):
        print(self.result)


first = Avenger()
second = Avenger()
first.set_name('Thor')
second.set_name('Hulk')
b = Battle()
b.battle(first, second)
b.who_win()
