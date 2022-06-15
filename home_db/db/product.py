from sqlalchemy import Column, ForeignKey, Integer, String

from db.database import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name_product = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)

    def __init__(self, name_product, price, count):
        self.name_product = name_product
        self.price = price
        self.count = count

    def __repr__(self):
        return f"Товар (Наименование: {self.name_product}, Цена: {self.price}, Остаток на складе: {self.count})"
