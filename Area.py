# This is meant to be use as a library and it shouldn't be edited by anyone.

shapes = {'Square': ['Length '],
          'Rectangle': ['Length', 'Breadth'],
          'Circle': ['Radius'],
          'Triangle': ['Base', 'Height'],
          'Parallelogram': ['Base', 'Height'],
          'Rhombus': ['Diagonal1', 'Diagonal2'],
          'Trapezium': ['Sum of parallel side', 'Height']}


# =====Square====
class Square(object):
    def __init__(self, length):
        self.area = int(length**2)


# =====Rectangle====
class Rectangle(object):
    def __init__(self, length, breadth):
        self.area = int(length*breadth)


# =====Circle====
class Circle(object):
    def __init__(self, radius):
        self.area = int(3.1416*radius*radius)


# =====Triangle====
class Triangle(object):
    def __init__(self, base, height):
        self.area = int(0.5*base*height)


# =====Parallelogram====
class Parallelogram(object):
    def __init__(self, base, height):
        self.area = int(base*height)


# =====Rhombus====
class Rhombus(object):
    def __init__(self, diagonal1, diagonal2):
        self.area = int(diagonal1*diagonal2)


# =====Trapezium====
class Trapezium(object):
    def __init__(self, sumofside, height):
        self.area = int(sumofside*height * 0.5)


if __name__ == '__main__':
    print("This will be printed when this file in not used as library.")
