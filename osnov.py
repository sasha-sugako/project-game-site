from flask import Flask
from flask import render_template, redirect
import sqlite3
con = sqlite3.connect("game.db")
cur = con.cursor()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/game', methods=['GET', 'POST'])
def login():
    params = {}
    return render_template('secur.html', **params)


@app.route('/success')
def success():
    params = {'form': {
              'title': obr_vop()[0]}}
    return render_template('seccess.html', **params)


def obr_vop():
    result = cur.execute("""SELECT vopr FROM second_page WHERE num_v = 1""").fetchall()
    a = []
    a.append(result[0][0])
    print(a)
    return a


def normal_form(text):
    return text

obr_vop()
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')