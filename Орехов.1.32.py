class Controller:
    def __init__(self):
        self.article_model = FilmModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film = self.user_interface.add_film()
            self.article_model.add_film(film)
        elif answer == "2":
            films = self.article_model.get_cat_films()
            self.user_interface.show_cat_films(films)
        elif answer == "3":
            film_name = self.user_interface.get_user_film()
            try:
                film = self.article_model.get_single_film(film_name)
            except KeyError:
                self.user_interface.show_incorrect_film_name_error(film_name)
            else:
                self.user_interface.show_single_film(film)
        elif answer == "4":
            film_name = self.user_interface.get_user_film()
            try:
                film = self.article_model.remove_film(film_name)
            except KeyError:
                self.user_interface.show_incorrect_film_name_error(film_name)
            else:
                self.user_interface.remove_single_film(film)
        elif answer == "q":
            self.article_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)


# _______________________________________________________________________________________________
# _______________________________________________________________________________________________
# _______________________________________________________________________________________________
import pickle
import os.path


class Film:
    def __init__(self, name, genre, reg, year, time, prod, actors):
        self.name = name
        self.genre = genre
        self.reg = reg
        self.year = year
        self.time = time
        self.prod = prod
        self.actors = actors

    def __str__(self):
        return f"{self.name} режиссера {self.reg}"


class FilmModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.films = self.load_data()

    def add_film(self, dict_films):
        film = Film(*dict_films.values())
        self.films[film.name] = film

    def get_cat_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_films = {"название фильма": film.name,
                      "жанр": film.genre,
                      "режиссер": film.reg,
                      "год выпуска": film.year,
                      "длительность": film.time,
                      "студия": film.prod,
                      "актеры": film.actors}
        return dict_films

    def remove_film(self, film_name):
        return self.films.pop(film_name)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as file:
                return pickle.load(file)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, "wb") as file:
            pickle.dump(self.films, file)


# _______________________________________________________________________________________________
# _______________________________________________________________________________________________
# _______________________________________________________________________________________________


def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface:
    @add_title(" Редактирование данных каталога фильмов ")
    def wait_user_answer(self):
        print("Действия с фильмами: ")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Добаление фильма")
    def add_film(self):
        dict_films = {"название фильма": None,
                      "жанр": None,
                      "режиссер": None,
                      "год выпуска": None,
                      "длительность": None,
                      "студия": None,
                      "актеры": None}
        for key in dict_films:
            dict_films[key] = input(f"Введите {key} фильма: ")
        return dict_films

    @add_title("Каталог фильмов:")
    def show_cat_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")

    @add_title("Ввод названия фильма: ")
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр фильма: ")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_title("Сообщение об ошибке: ")
    def show_incorrect_film_name_error(self, film_name):
        print(f"Фильма с названием '{film_name}' не существует")

    @add_title("Удаление фильма: ")
    def remove_single_film(self, film):
        print(f"Фильм с названием '{film}' удален")

    @add_title("Сообщение об ошибке: ")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта с названием '{answer}' не существует")


# _______________________________________________________________________________________________
# _______________________________________________________________________________________________
# _______________________________________________________________________________________________


def main():
    app = Controller()
    app.run()


if __name__ == "__main__":
    main()

print("_______________________________________________________________________")
