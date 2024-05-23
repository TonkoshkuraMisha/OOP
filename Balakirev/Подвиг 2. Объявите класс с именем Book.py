import sys


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


# Считывание списка из входного потока (эту строчку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# Создание объекта класса Book с использованием данных из lst_in
title, author, pages = lst_in[0], lst_in[1], int(lst_in[2])
book = Book(title, author, pages)

# Вывод строкового представления объекта book
print(book)
