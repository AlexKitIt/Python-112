
import math


class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def summm(self):
        print(f"Сумма: {self.a + self.b}")

    def mult(self):
        print(f"Произведение: {self.a * self.b}")

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b


class RightTriangle(Pair):
    def g(self):
        return round(math.sqrt((self.a ** 2) + (self.b ** 2)), 2)

    def gip(self):
        print(f"Гипотенуза △ABC: {RightTriangle.g(self)}")

    def info(self):
        print(f"Прямоугольный треугольник △ABC ({self.a}, {self.b}, {RightTriangle.g(self)})")

    def square(self):
        print(f"Площадь △ABC : {0.5 * (self.a * self.b)}")


tr = RightTriangle(5, 8)
tr.gip()
tr.info()
tr.square()
print()
tr.summm()
tr.mult()
print()
tr.a = 10
tr.gip()
tr.b = 20
tr.gip()
tr.summm()
tr.mult()
tr.square()
print("_______________________________________________________________________")


