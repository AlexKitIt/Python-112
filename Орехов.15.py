import math


def area(figure_type, **kwargs):
    s = 1
    if figure_type == "rhombus":
        for i in kwargs:
            s *= kwargs[i]
        print(s / 2)
    elif figure_type == "square":
        for i in kwargs:
            s = kwargs[i] ** 2
        print(s)
    elif figure_type == "trapezoid":
        a = kwargs["a"]
        b = kwargs["b"]
        h = kwargs["h"]
        s = 0.5 * (a + b) * h
        print(s)
    elif figure_type == "circle":
        s = math.pi * (kwargs["r"] ** 2)
        print(s)
    else:
        print("invalid data")


area("rhombus", d1=10, d2=8)
area("square", a=5)
area("trapezoid", a=12, b=3, h=6)
area("circle", r=18)
area("unknown", a=1, b=2, c=3)