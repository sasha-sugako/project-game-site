from flask import Flask
from flask import render_template, redirect
import random
from data import db_session
from requests import request
con = sqlite3.connect("game.db")
cur = con.cursor()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/game', methods=['GET', 'POST'])
def login():
    params = {
        'vopr': ['Фильмы', 'Книги', 'Фауна', 'Еда', 'Солянка'],
        'list': [10, 20, 30, 40, 50],
        'id_vopr': [1, 2, 3, 4, 5]
    }
    return render_template('secur.html', **params)

    
@app.route('/success')
def success():
    params = {'form': {
        'vopr': obr_vop(num_vopr)
    }}
    return render_template('seccess.html', **params)


def obr_vop(num_vopr):
    result = []
    for i in session.query(Second_page).filter(Second_page.kol_isp == 0, Second_page.vopr_id == num_vopr):
        result.append(i)
    a = random.randint(0, len(result))
    vopr_ud = session.query(Second_page).filter(Second_page.title == result[a][0])
    vopr_ud.kol_isp = 1
    session.commit()
    return result[a][0]


if __name__ == '__main__':
    db_session.global_init("db/game.sqlite")
    app.run(port=8080, host='127.0.0.1')