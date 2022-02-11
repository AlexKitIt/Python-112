import math


def sq(form):
    if form == 1:
        a = int(input("Введите длину прямоугольника: "))
        b = int(input("Введите ширину прямоугольника: "))
        s = a * b
    if form == 2:
        a = int(input("Введите основание треугольника: "))
        b = int(input("Введите высоту треугольника: "))
        s = 0.5 * (a * b)
    if form == 3:
        a = int(input("Введите радиус круга: "))
        s = math.pi * a ** 2
    print("Площадь:", round(s, 2))

sq(int(input("Укажите фигуру для определения площади: 1-прямоугольник, 2-треугольник, 3-круг: ")))
# ___________________________________________________________________________________________________
def fun(lst):
    simple = []
    not_simple = []
    for i in lst:
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                not_simple.append(i)
        else:
            simple.append(i)
    print("Min: ", min(simple))
    print("Max: ", max(not_simple))

fun([6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1])
