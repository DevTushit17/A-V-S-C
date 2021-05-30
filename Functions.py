import Area
import Volume

def Connect(quantity, shape, values):
    if quantity == 'Area':
        if shape == 'Square':
            obj = Area.Square(values[0])
            return obj.area
        elif shape == 'Rectangle':
            obj = Area.Rectangle(values[0], values[1])
            return obj.area
        elif shape == 'Circle':
            obj = Area.Circle(values[0])
            return obj.area
        elif shape == 'Triangle':
            obj = Area.Triangle(values[0], values[1])
            return obj.area
        elif shape == 'Parallelogram':
            obj = Area.Parallelogram(values[0], values[1])
            return obj.area
        elif shape == 'Rhombus':
            obj = Area.Rhombus(values[0], values[1])
            return obj.area
        elif shape == 'Trapezium':
            obj = Area.Trapezium(values[0], values[1])
            return obj.area

    elif quantity == 'Volume':
        if shape == 'Cube':
            obj = Volume.Cube(values[0])
            return obj.volume
        elif shape == 'Cuboid':
            obj = Volume.Cuboid(values[0], values[1], values[2])
            return obj.volume
        elif shape == 'Sphere':
            obj = Volume.Sphere(values[0])
            return obj.volume
        elif shape == 'Cone':
            obj = Volume.Cone(values[0], values[1])
            return obj.volume
        elif shape == 'Cylinder':
            obj = Volume.Cylinder(values[0], values[1])
            return obj.volume

    elif quantity == 'Surface Area':
        if shape == 'Cube':
            obj = Volume.Cube(values[0])
            return obj.tsa
        elif shape == 'Cuboid':
            obj = Volume.Cuboid(values[0], values[1], values[2])
            return obj.tsa
        elif shape == 'Sphere':
            obj = Volume.Sphere(values[0])
            return obj.tsa
        elif shape == 'Cone':
            obj = Volume.Cone(values[0], values[1])
            return obj.tsa
        elif shape == 'Cylinder':
            obj = Volume.Cylinder(values[0], values[1])
            return obj.tsa


if __name__ == '__main__':
    print(" NSFW Warning"+
    "\n DON'T FUCKING TOUCH IT !!, there is nothing for you here."+
        "\n If your program doesn't work properly after you edit this file, then that's your problem.")
