class Weight:
    def __init__(self, w):
        self.__w = w

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, w):
        if isinstance(w, int):
            self.__w = w
        else:
            raise ValueError("Неверный формат данных")

    @w.deleter
    def w(self):
        del self.__w

    def transformation(self):
        return self.__w * 2.2


w1 = Weight(12)
w1.w = 12
print(f"{w1.w} кг => {round(w1.transformation(),1)} фунтов")

w2 = Weight(41)
w2.w = 41
print(f"{w2.w} кг => {round(w2.transformation(),1)} фунтов")
print("_______________________________________________________________________")



