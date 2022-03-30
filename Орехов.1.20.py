class Book:
    name = ""
    year = ""
    publisher = ""
    genre = ""
    author = ""
    price = ""

    def input_info(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def print_info(self):
        print(" Книга ".center(40, "*"))
        print(f"Название: {self.name}\nГод выпуска: {self.year}\nИздатель: {self.publisher}\nЖанр: {self.genre}\nАвтор: {self.author}\nЦена: {self.price}")
        print("*"*40)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


b1 = Book()
b1.input_info("Государь", "2018", "Азбука", "Художественный вымысел", "Никколо Макиавелли", "252")
b1.print_info()
b1.set_genre("эссе")
print(b1.get_genre())
print("_______________________________________________________________________")



