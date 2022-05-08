class Person:
    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.skill = q

    def __del__(self):
        print(f"До свидания, мистер {self.name}.{self.surname}.")

    def info(self):
        return f"{self.name}.{self.surname}, {self.skill}."


staff = [Person("И", "Крысов", 3),
         Person("Д", "Мышев", 1),
         Person("O", "Жуков", 2)]
for person in staff:
    print(person.info())
staff.sort(key=lambda p: p.skill, reverse=True)
del staff[-1]
print("Конец программы")
input()
