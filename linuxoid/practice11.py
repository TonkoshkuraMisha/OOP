from random import random


def random_generator(qty, minimum, maximum):
    while qty > 0:
        yield random() * (maximum - minimum) + minimum
        qty -= 1


a = random_generator(5, -2, 2)
for i in a:
    print(round(i, 2))
