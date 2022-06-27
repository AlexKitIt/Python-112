import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM menu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из базы данных")
        return []

    def add_pet(self, name, petname, description):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO pets VALUES(NULL, ?, ?, ?, ?)", (name, petname, description, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления питомца в БД" + str(e))
            return False
        return True

    def get_one_pet(self, petname):
        try:
            self.__cur.execute(f"SELECT petname, description FROM pets WHERE petname LIKE '{petname}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения конкретного питомца из БД" + str(e))
        return False, False

    def get_all_pets(self):
        try:
            self.__cur.execute(f"SELECT name, petname, description FROM pets ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения списка питомцев из БД" + str(e))
        return []

    def get_one_pet_on_user(self, username):
        try:
            self.__cur.execute(f"SELECT name, petname FROM pets WHERE name LIKE '{username}' LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения конкретного питомца по владельцу из БД" + str(e))
        return False, False
