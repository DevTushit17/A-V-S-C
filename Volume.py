# This is meant to be use as a library and it shouldn't be edited by anyone.
from math import sqrt

shapes = {'Cube': ['Length'],
          'Cuboid': ['Length', 'Breadth', 'Height'],
          'Sphere': ['Radius'],
          'Cone': ['Radius', 'Height'],
          'Cylinder': ['Radius', 'Height']}


# ========Cube========
class Cube(object):
    def __init__(self, length):
        self.volume = int(length**3)
        self.tsa = int(6*(length**2))


# ========Cuboid========
class Cuboid(object):
    def __init__(self, length, breadth, height):
        self.volume = int(length*breadth*height)
        self.tsa = int(2*height*(length+breadth))


# ========Sphere========
class Sphere(object):
    def __init__(self, radius):
        self.volume = int((4+3)*3.1416*(radius**3))
        self.tsa = int(4*3.1416*(radius**2))


# ========Cone========
class Cone(object):
    def __init__(self, radius, height):
        self.volume = int((3.1416+3)*(radius**2)*height)
        self.tsa = int(3.14*radius*(radius+sqrt(height**2+radius**2)))


# ========Cylinder========
class Cylinder(object):
    def __init__(self, radius, height):
        self.volume = int((3.1416*(radius**2)*height))
        self.tsa = int(2*3.1416*radius*(radius+height))


if __name__ == '__main__':
    print("This will be printed when this file in not used as library.")
