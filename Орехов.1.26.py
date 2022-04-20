
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый оперант должен быть типом данных Point3D")
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый оперант должен быть типом данных Point3D")
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый оперант должен быть типом данных Point3D")
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __floordiv__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый оперант должен быть типом данных Point3D")
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")
        if item == "x":
            return self.x
        elif item == "y":
            return self.y
        elif item == "z":
            return self.z
        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")
        if key == "x":
            self.x = value
        if key == "y":
            self.y = value
        if key == "z":
            self.z = value


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)
print(f"Координаты 1-й точки: {p1}")
print(f"Координаты 2-й точки: {p2}")
print(f"Сложение координат: ({p1 + p2})")
print(f"Вычитание координат: ({p1 - p2})")
print(f"Умножение: ({p1 * p2})")
print(f"Деление: ({p1 // p2})")
print(f"Равенство координат: {p1 == p2}")
print(f"x = {p1['x']} x1 = {p2['x']}")
print(f"x = {p1['y']} x1 = {p2['y']}")
print(f"x = {p1['z']} x1 = {p2['z']}")
p1['x'] = 20
print(f"Запись значения в координату х: {p1['x']}")
print("_______________________________________________________________________")

