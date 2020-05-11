from flask import Flask
from flask import render_template, redirect
import random
from data import db_session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/game', methods=['GET', 'POST'])
def login():
    params = {'form': {
        'vopr': ['Фильмы', 'Книги', 'Фауна', 'Еда', 'Солянка'],
        'list': [10, 20, 30, 40, 50],
        'id_vopr': [1, 2, 3, 4, 5]
    }}
    return render_template('secur.html', **params)

    
@app.route('/films')
def films():
    params = {}
    return render_template('films.html', **params)


@app.route('/books')
def books():
    params = {}
    return render_template('books.html', **params)


@app.route('/animals')
def animals():
    params = {}
    return render_template('animals.html', **params)


@app.route('/units')
def units():
    params = {}
    return render_template('units.html', **params)


@app.route('/hodgepodge')
def hodgepodge():
    params = {}
    return render_template('hodgepodge.html', **params)


def obr_vop(num_vopr):
    result = []
    session = db_session.create_session()
    for i in session.query(Second_page).filter(Second_page.kol_isp == 0, Second_page.vopr_id == num_vopr):
        result.append(i)
    a = random.randint(0, len(result))
    vopr_ud = session.query(Second_page).filter(Second_page.title == result[a][0])
    vopr_ud.kol_isp = 1
    session.commit()
    return result[a][0]


def name_vopr():
    session = db_session.create_session()
    result = []
    for i in session.query(First_page).all():
        result.append(i.tema_vopr)
    return result
    
#params = {'form': {
#        'vopr': obr_vop(num_vopr)
#    }}
if __name__ == '__main__':
    db_session.global_init("db/game.sqlite")
    app.run(port=8080, host='127.0.0.1')