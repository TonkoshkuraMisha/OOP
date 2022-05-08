"""
    Объектная картина мира:
    - Системы (как реальные, так и цифровые) состоят из объектов;
    - Объекты могут воздействовать друг на друга. В результате их свойства могут меняться;
    - Задача решается путём создания подходящих объектов и организации их взаимодействия.

    В языке Python класс равносилен понятию тип данных.

    В Python все классы сами являються объектами класса type. Точно так же все модули
    являются объектами класса module.

    Во избежание путаницы объекты, созданные на основе обычных классов, называют экземплярами.

    Наследование.
        Основное преимущество, которое даёт концепция наследования - это вынос одинакового кода из
        разных дочерних классов в один родительский класс. Наследование позволяет свести на нет
        повторение кода в разных частях программы.

    Инкапсуляция.
        Понимается двояко:
        - Сокрытие данных, т.е. невозможность напрямую получить доступ к внутренней структуре
        объекта, так как это небезопасно. В Python нет такой инкапсуляции.
        - Объединение описания свойств объектов и их поведения в единое целое, т.е. в класс.
        Инкапсуляция в этом смысле - сама суть ООП и присутствует во всех ОО-языках.

    Полиморфизм.
        - Объекты разных классов, с разной внутренней реализацией, т.е. программным кодом,
        могут иметь "одинаковые" методы. На самом деле у методов совпадают только имена, а
        вложенный в них код (то, что они делают) различен. Вот и получается что у одного имени,
        как бы, множество форм.
        Пример. Полиморфизм операции "+":
            - для чисел, это обычное сложение;
            - для строк, это конкатенация;
        - Если у объектов разных классов есть одноимённый метод, то коллекция таких разнородных
        объектов может быть обработана в одном цикле.
"""


class A:
    field1 = 1

    def make_str(self):
        print(self.field1)


class B(A):
    field2 = 2

    def make_str(self):
        print(self.field1, self.field2)


class C(A):
    field3 = 3

    def make_str(self):
        print(self.field1, self.field3)


a = A()
b = B()
c = C()

for i in (a, b, c):
    i.make_str()