class Point:
    """
    class creat and give coords of points
    """
    color = 'red'
    circle = 2

    def __init__(self):
        self.y = None
        self.x = None

    def set_coords(self, x, y):
        self.x = x
        self.y = y


pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)
print(pt.__doc__)
