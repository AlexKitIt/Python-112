import os
import sqlite3

from flask import Flask, render_template, url_for, request, session, redirect, abort, g
from app.FDataBase import FDataBase

DATABASE = '/tmp/db.db'
DEBUG = True
SECRET_KEY = "12345678901234567890"


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, "db.db")))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@ app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", title="Главная", menu=dbase.get_menu())


@app.route("/about")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("about.html", title="О нас", menu=dbase.get_menu())


@app.route("/login", methods=["POST", "GET"])
def login():
    db = get_db()
    dbase = FDataBase(db)
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == "alex" and request.form['password'] == "123456":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template("login.html", title="Авторизация", menu=dbase.get_menu())


@app.route("/profile/<username>")
def profile(username):
    db = get_db()
    dbase = FDataBase(db)
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return render_template("profile.html", title="Профиль пользователя", menu=dbase.get_menu(),
                           username=username)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page404.html", title="Страница не найдена")


if __name__ == "__main__":
    app.run(debug=True)
