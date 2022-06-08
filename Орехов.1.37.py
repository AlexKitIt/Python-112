import sqlite3 as sq

goods = [
    (1, 'Картофель', 20),
    (1, 'Томаты', 30),
    (1, 'Оругцы', 25),
    (1, 'Свекла', 22),
    (1, 'Капуста', 18),
    (2, 'Апельсин', 32),
    (2, 'Ананас', 40),
    (2, 'Мандарин', 38),
    (3, 'Молоток', 15),
    (3, 'Отвертка', 10),
    (3, 'Скотч', 5)
]
sellers = [
    (1, 'Мир овощей'),
    (2, 'Мир фруктов'),
    (3, 'Инструменты')
]

with sq.connect("orders.db") as con:
    cur = con.cursor()
    cur.executescript(
        """CREATE TABLE IF NOT EXISTS prod(
        kod_sale INTEGER,
        product TEXT,
        price INTEGER,
        FOREIGN KEY (kod_sale)  REFERENCES sellers(id));
        CREATE TABLE IF NOT EXISTS sellers(
        id INTEGER PRIMARY KEY,
        seller TEXT,
        FOREIGN KEY (id)  REFERENCES prod(kod_sale))
        """)
    cur.executemany("INSERT INTO prod VALUES(?, ?, ?)", goods)
    cur.executemany("INSERT INTO sellers VALUES(?, ?)", sellers)

print("_______________________________________________________________________")
