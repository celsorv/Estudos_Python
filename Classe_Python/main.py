class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return self.x, self.y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        #return '(' + str(self.x) + ',' + str(self.y) + ')'
        return '({},{})'.format(self.x, self.y)

    # x + y ==> (2, 3) + (2, 2) => (4, 5)
    # x + 8 ==> (2, 3) + 8 => (10, 11)
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)

    # x + y ==> (2, 3) - (2, 2) => (0, 1)
    # x + 8 ==> (2, 3) - 8 => (-6, -5)
    def __sub__(self, other):
        if type(other) == Point:
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other, self.y - other)

    # x * y ==> (2, 3) * (2, 2) => (4, 6)
    # x * 8 ==> (2, 3) * 8 => (16, 24)
    def __mul__(self, other):
        if type(other) == Point:
            return Point(self.x * other.x, self.y * other.y)
        else:
            return Point(self.x * other, self.y * other)

    # x / y ==> (2, 3) / (2, 2) => (1, 1.5)
    # x / 8 ==> (2, 3) / 8 => (0.25, 0.375)
    def __truediv__(self, other):
        if type(other) == Point:
            return Point(self.x / other.x, self.y / other.y)
        else:
            return Point(self.x / other, self.y / other)

    # x // y ==> (2, 3) // (2, 2) => (1, 1)
    # x // 8 ==> (2, 3) // 8 => (0, 0)
    def __floordiv__(self, other):
        if type(other) == Point:
            return Point(self.x // other.x, self.y // other.y)
        else:
            return Point(self.x // other, self.y // other)

    # x % y ==> (2, 3) % (2, 2) => (0, 1)
    # x % 8 ==> (2, 3) % 8 => (2, 3)
    def __mod__(self, other):
        if type(other) == Point:
            return Point(self.x % other.x, self.y % other.y)
        else:
            return Point(self.x % other, self.y % other)

    def __eq__(self, other):
        if type(other) == Point:
            return self.x == other.x and self.y == other.y
        else:
            return self.x == other and self.y == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if type(other) == Point:
            return self.x > other.x or (self.x == other.x and self.y > other.y)
        else:
            return self.x > other or (self.x == other and self.y > other)
            

p = Point(3, 3)
q = Point(3, 3)

print(p != q)
print(p == 3)

