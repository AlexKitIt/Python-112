
class Clock:
    __Day = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть числом")

        self.__sec = sec % self.__Day

    def det_format_time(self):
        s = self.__sec % 60
        m = (self.__sec // 60) % 60
        h = (self.__sec // 3600) % 24
        return f"{Clock.__det_form(h)}:{Clock.__det_form(m)}:{Clock.__det_form(s)}"

    @staticmethod
    def __det_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.__sec

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый оперант должен быть типом данных Clock")
        return Clock(self.__sec + other.get_seconds())

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый оперант должен быть типом данных Clock")
        return Clock(self.__sec - other.get_seconds())

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый оперант должен быть типом данных Clock")
        return Clock(self.__sec * other.get_seconds())

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый оперант должен быть типом данных Clock")
        return Clock(self.__sec // other.get_seconds())

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый оперант должен быть типом данных Clock")
        return Clock(self.__sec % other.get_seconds())

    # def __isub__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый оперант должен быть типом данных Clock")
    #     return Clock(self.__sec - other.__sec)
    #
    # def __imul__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый оперант должен быть типом данных Clock")
    #     return Clock(self.__sec * other.__sec)
    #
    # def __ifloordiv__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый оперант должен быть типом данных Clock")
    #     return Clock(self.__sec // other.__sec)
    #
    # def __imod__(self, other):
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый оперант должен быть типом данных Clock")
    #     return Clock(self.__sec % other.__sec)


c1 = Clock(600)
c2 = Clock(200)
c1_1 = c1
c3 = c1_1 - c2
c4 = c1_1  * c2
c5 = c1_1  // c2
c6 = c1_1  % c2
c7 = c1_1  = c1 - c2
c8 = c1_1  = c1_1 * c2
c9 = c1_1  = c1_1  // c2
c10 = c1_1  = c1_1  % c2
print(f"c1: {c1.det_format_time()}")
print(f"c1 - c2: {c3.det_format_time()}")
print(f"c1 * c2: {c4.det_format_time()}")
print(f"c1 // c2: {c5.det_format_time()}")
print(f"c1 % c2: {c6.det_format_time()}")
print(f"c1 -= c2: {c7.det_format_time()}")
print(f"c1 *= c2: {c8.det_format_time()}")
print(f"c1 //= c2: {c9.det_format_time()}")
print(f"c1 %= c2: {c10.det_format_time()}")
print("_______________________________________________________________________")

