import os

from sqlalchemy import and_, desc, distinct

from db.database import DATABASE_NAME, Session
import create_db as db_creator
from db.product import Product

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    print(session.query(Product).count())
    print("*" * 60)
    print(session.query(Product).get(19))
    print("*" * 60)
    for p in session.query(Product).filter(Product.name_product == "Малина"):
        print(p)
    print("*" * 60)
    for p in session.query(Product).filter(and_(Product.name_product.like("А%"), Product.price > 300)):
        print(p)
    print("*" * 60)
    print(session.query(Product).filter(Product.price is None).all())
    print("*" * 60)
    for p in session.query(Product).filter(Product.price.between(200, 300)):
        print(p)
    print("*" * 60)
    for p in session.query(Product).order_by(desc(Product.count)):
        print(p)
    print("*" * 60)
    print("*" * 60)
    for p in session.query(distinct(Product.name_product)):
        print(p)
    print("*" * 60)
    v = session.query(Product).get(7)
    v.name_product = "Виноград"
    session.add(v)
    session.commit()
    for p in session.query(Product):
        print(p)
    print("*" * 60)
    session.add(Product(name_product="Гранат", price=230, count=3))
    session.commit()
    for p in session.query(Product):
        print(p)
    print("*" * 60)

