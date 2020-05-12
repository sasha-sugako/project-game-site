from flask import Flask
from flask import render_template, redirect
import random
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from data import db_session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
k = 0


@app.route('/game', methods=['GET', 'POST'])
def login():
    params = {'form': {
        'vopr': ['Фильмы', 'Книги', 'Фауна', 'Еда', 'Солянка'],
        'id_vopr': [1, 2, 3, 4, 5]
    }}
    return render_template('secur.html', **params)

    
@app.route('/films', methods=['GET', 'POST'])
def films():
    global k
    form = AnswerForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(Second_page).filter(Second_page.otve == form.answer.data).first():
            k += 10
        session.commit()
        return redirect('/game')
    return render_template('films.html', form=form)


@app.route('/books', methods=['GET', 'POST'])
def books():
    global k
    form = AnswerForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(Second_page).filter(Second_page.otve == form.answer.data).first():
            k += 10
        session.commit()
        return redirect('/game')
    return render_template('books.html', form=form)


@app.route('/animals', methods=['GET', 'POST'])
def animals():
    global k
    form = AnswerForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(Second_page).filter(Second_page.otve == form.answer.data).first():
            k += 10
        session.commit()
        return redirect('/game')
    return render_template('animals.html', form=form)


@app.route('/units', methods=['GET', 'POST'])
def units():
    global k
    form = AnswerForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(Second_page).filter(Second_page.otve == form.answer.data).first():
            k += 10
        session.commit()
        return redirect('/game')
    return render_template('units.html', form=form)


@app.route('/hodgepodge', methods=['GET', 'POST'])
def hodgepodge():
    global k
    form = AnswerForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(Second_page).filter(Second_page.otve == form.answer.data).first():
            k += 10
        session.commit()
        return redirect('/game')
    return render_template('hodgepodge.html', form=form)


@app.route('/result_of_game')
def result_of_game():
    global k
    params = {
        'form':{
            'kol_ball': k,
            'title': ['Думаю вам надо ещё потренироваться',
                      'Неплохой результат',
                      'Да вы просто мастер этой игры'],
        }
    }
    return render_template('result_of_game.html', **params)


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


class AnswerForm(FlaskForm):
    answer = TextAreaField("Ответ: ")
    submit = SubmitField('Отправить')


#params = {'form': {
#        'vopr': obr_vop(num_vopr)
#    }}
if __name__ == '__main__':
    db_session.global_init("db/game.sqlite")
    app.run(port=8080, host='127.0.0.1')