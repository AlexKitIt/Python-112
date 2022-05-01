
import math


class Circle:
    def __init__(self, rad):
        self.radius = rad

    def __str__(self):
        return f"Радиус: {self.radius}"

    def length(self):
        # print("Длина окружности:", end=" ")
        return round((2 * math.pi * self.radius), 2)

    def area(self):
        # print("Площадь круга:", end=" ")
        return round((math.pi * (self.radius ** 2)), 2)


class Rectangle:
    def __init__(self, a, b):
        self.length = a
        self.width = b

    def __str__(self):
        return f"Стороны: {self.length}, {self.width}"

    def perimeter(self):
        # print("Периметр прямоугольника:", end=" ")
        return round(2 * (self.length + self.width), 2)

    def area(self):
        return round((self.length * self.width), 2)


class Cylinder(Circle):
    def __init__(self, h, rad):
        super().__init__(rad)
        self.height = h

    def capacity(self):
        return round((self.area() * self.height), 2)


#Окружности
c1 = Circle(1)
c2 = Circle(2)
c3 = Circle(3)
c4 = Circle(4)
c5 = Circle(5)
c6 = Circle(6)
c7 = Circle(7)
c8 = Circle(8)
c9 = Circle(9)
c10 = Circle(10)
#Прямоугольники
r1 = Rectangle(5, 5)
r2 = Rectangle(2, 7)
r3 = Rectangle(10, 21)
#Цилиндры
cy1 = Cylinder(7, 4)
cy2 = Cylinder(5, 2)
cy3 = Cylinder(3, 9)
cy4 = Cylinder(5, 5)

print("Длина окружности:", c4.length())
print("Длина окружности:", c2.length())
print("Длина окружности:", c9.length())
print("Длина окружности:", c5.length())

print("Площадь круга:", c4.area())
print("Площадь круга:", c2.area())
print("Площадь круга:", c6.area())
print("Площадь круга:", c8.area())
print("Площадь круга:", c1.area())

print("Периметр:", r1.perimeter())
print("Периметр:", r2.perimeter())
print("Периметр:", r3.perimeter())

print("Площадь круга:", cy1.area(), "\nОбъем:", cy1.capacity())
print("Площадь круга:", cy2.area(), "\nОбъем:", cy2.capacity())
print("Площадь круга:", cy3.area(), "\nОбъем:", cy3.capacity())
print("Площадь круга:", cy4.area(), "\nОбъем:", cy4.capacity())


def comparison(*args):
    if isinstance(args[0], Rectangle):
        print("Прямоугольник с наименьшим периметром:", end=" ")
        i = 0
        min_per = args[i].perimeter()
        ind = 0
        while i < len([*args])-1:
            if args[i+1].perimeter() < min_per:
                min_per = args[i+1].perimeter()
                ind = i+1
            i += 1
        return print(args[ind])
    if isinstance(args[0], Cylinder):
        print("Средний объем всех цилиндров:", end=" ")
        i = 0
        cap = 0
        while i < len([*args]):
            cap += args[i].capacity()
            i += 1
        return print(round(cap/len([*args]), 2))
    if isinstance(args[0], Circle):
        print("Окружность с наибольшей площадью:", end=" ")
        i = 0
        max_ar = args[i].area()
        ind = 0
        while i < len([*args]) - 1:
            if args[i + 1].area() > max_ar:
                max_ar = args[i + 1].area()
                ind = i + 1
            i += 1
        return print(args[ind])


print("*" * 40)
comparison(c1, c5, c8)
comparison(r1, r2, r3)
comparison(cy1, cy2, cy3, cy4)


def comparison2(*args):
    rec = []
    cir = []
    cyl = []
    for y in args:
        if isinstance(y, Rectangle):
            rec.append(y)
        if isinstance(y, Circle) and not isinstance(y, Cylinder):
            cir.append(y)
        if isinstance(y, Cylinder):
            cyl.append(y)
    if len(cir) != 0:
        i = 0
        max_ar = cir[i].area()
        ind = 0
        while i < len(cir) - 1:
            if cir[i + 1].area() > max_ar:
                max_ar = cir[i + 1].area()
                ind = i + 1
            i += 1
        print("Окружность с наибольшей площадью:", cir[ind])
    if len(rec) != 0:
        min_per = rec[0].perimeter()
        i = 0
        ind = 0
        while i < len(rec) - 1:
            if rec[i + 1].perimeter() < min_per:
                min_per = rec[i + 1].perimeter()
                ind = i + 1
            i += 1
        print("Прямоугольник с наименьшим периметром:", rec[ind])
    if len(cyl) != 0:
        i = 0
        cap = 0
        while i < len(cyl):
            cap += cyl[i].capacity()
            i += 1
        print("Средний объем всех цилиндров:", round(cap / len(cyl), 2))


print("*" * 40)
comparison2(c1, r1, cy1, c5, r2, cy2, c8, r3, cy3, cy4)
print("_______________________________________________________________________")

