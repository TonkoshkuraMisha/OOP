class Point:
    color = 'red'
    circle = 2
    radius = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

    def get_rad(self):
        return pow(((self.x) ** 2 + (self.y) ** 2), 0.5)


pt1 = Point(2, 3)
pt2 = Point(5, -2)
print(pt1.__dict__)
print(pt2.__dict__)
print(pt1.get_rad())
print(pt2.get_rad())
