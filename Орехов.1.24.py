
import math
from abc import ABC, abstractmethod


class Radical(ABC):
    @abstractmethod
    def calculation(self):
        print("Корень уравнения", end=" ")


class LinearEquation(Radical):
    def calculation(self):
        print("Введите коэффициенты для уравнения")
        print("ax + b = 0:")
        a = float(input("a = "))
        b = float(input("b = "))
        if (a == 0 and b == 0) or (a == 0 and b != 0):
            print("Корней данного уравнения нет")
        elif a != 0:
            super().calculation()
            print(f"{round(a)}x + ({round(b)}): {round((-b / a), 2)}")


class SquareEquation(Radical):
    def calculation(self):
        print("Введите коэффициенты для уравнения")
        print("ax^2 + bx + c = 0:")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        discr = b ** 2 - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            super().calculation()
            print(f"{round(a)}x^2 + ({round(b)})x + ({round(c)}): {round(x1, 2)}, {round(x2, 2)}")
        elif discr == 0:
            x = -b / (2 * a)
            super().calculation()
            print(f"{round(a)}x^2 + ({round(b)})x + ({round(c)}): {round(x, 2)}")
        else:
            print("Корней данного уравнения нет")

# l1 = LinearEquation()
# l1.calculation()
# s1 = SquareEquation()
# s1.calculation()
print("_______________________________________________________________________")
import math
from abc import ABC, abstractmethod


class Radical(ABC):
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def calc(self):
        print("Корни уравнения", end=" ")


class Line(Radical):
    def calc(self):
        if (self.a == 0 and self.b == 0) or (self.a == 0 and self.b != 0):
            print("Корней данного уравнения нет")
        elif self.a != 0:
            super().calc()
            print(f"{round(self.a)}x + ({round(self.b)}): {round((-self.b / self.a), 2)}")


class Sq(Radical):
    def calc(self):
        discr = self.b ** 2 - 4 * self.a * self.c
        if discr > 0:
            x1 = (-self.b + math.sqrt(discr)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discr)) / (2 * self.a)
            super().calc()
            print(f"{round(self.a)}x^2 + ({round(self.b)})x + ({round(self.c)}): {round(x1, 2)}, {round(x2, 2)}")
        elif discr == 0:
            x = -self.b / (2 * self.a)
            super().calc()
            print(f"{round(self.a)}x^2 + ({round(self.b)})x + ({round(self.c)}): {round(x, 2)}")
        else:
            print("Корней данного уравнения нет")

l1 = Line(3, 7)
l1.calc()
s1 = Sq(1, -2, -3)
s1.calc()
print("_______________________________________________________________________")

