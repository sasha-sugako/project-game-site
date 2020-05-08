from flask import Flask
from flask import render_template, redirect
import sqlite3
import random
from data import db_session
con = sqlite3.connect("game.db")
cur = con.cursor()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/game', methods=['GET', 'POST'])
def login():
    params = {
        'vopr': ['Фильмы', 'Книги', 'Фауна', 'Еда', 'Солянка'],
        'list': [10, 20, 30, 40, 50]
    }
    return render_template('secur.html', **params)


@app.route('/success')
def success():
    params = {}
    return render_template('seccess.html', **params)


def obr_vop(num_vopr):
    result = cur.execute("""SELECT vopr FROM second_page WHERE num_v =""" + str(num_vopr)).fetchall()
    result2 = cur.execute("""SELECT kolvo_isp FROM second_page WHERE num_v =""" + str(num_vopr)).fetchall()
    a = random.randint(0, 4)
    while result2[a][0] != 0:
        a = random.randint(0, 4)
    otv = result[a][0]
    return otv


def normal_form(text):
    return text

print(obr_vop(1))
if __name__ == '__main__':
    db_session.global_init("db/blogs.sqlite")
    app.run(port=8080, host='127.0.0.1')