
import math


class Square:
    count = 0

    @staticmethod
    def square_triangle_geron(a, b, c):
        p = 0.5 * (a + b + c)
        print(f"Площадь треугольника по формуле Герона ({a},{b},{c}):", math.sqrt(p * (p - a) * (p - b) * (p - c)))
        Square.count += 1

    @staticmethod
    def square_triangle(a, h):
        print(f"Площадь треугольника по через основание и высоту ({a},{h}):", 0.5 * (a * h))
        Square.count += 1

    @staticmethod
    def square_area(a):
        print(f"Площадь квадрата ({a}):", a ** 2)
        Square.count += 1

    @staticmethod
    def square_rectangle(a, b):
        print(f"Площадь прямоугольника ({a},{b}):", a * b)
        Square.count += 1

    @staticmethod
    def return_count():
        print(f"Количество подсчетов площади: {Square.count}")


Square.square_triangle_geron(3, 4, 5)
Square.square_triangle(6, 7)
Square.square_area(7)
Square.square_rectangle(2, 6)
Square.return_count()
print("_______________________________________________________________________")



