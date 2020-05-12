from flask import Flask
from flask import render_template, redirect, url_for
import random
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from data import db_session
from data.second_page import Second_page
from data.first_page import First_page
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
k = 0
sp_f = []
sp_b = []
sp_a = []
sp_u = []
sp_h = []


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
    global sp_f
    title = obr_vop(1)
    print(title)
    if title == 'К сожалению вопросы закончились':
        params = {'form': {
            'title': title
        }}
        return render_template('bad.html', **params)
    else:
        right = right_answer(title)
        print(right)
        sp_f.append([title, right])
        img_this = img_vopr(title)
        form = AnswerForm()
        if form.validate_on_submit():
            if sp_f[-2][1] in form.answer.data.lower():
                k += 10
            return redirect('/game')
        return render_template('films.html', title=title, img_vopr=url_for('static', filename=img_this), form=form)


@app.route('/books', methods=['GET', 'POST'])
def books():
    global k
    title = obr_vop(2)
    if title == 'К сожалению вопросы закончились':
        params = {'form': {
            'title': title
        }}
        return render_template('bad.html', **params)
    else:
        img_this = img_vopr(title)
        form = AnswerForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            right_answer = session.query(Second_page).filter(Second_page.title == title).first()
            if right_answer.otve in form.answer.data.lower():
                k += 10
            session.commit()
            return redirect('/game')
        return render_template('books.html', title=title, img_vopr=url_for('static', filename=img_this), form=form)


@app.route('/animals', methods=['GET', 'POST'])
def animals():
    global k
    title = obr_vop(3)
    if title == 'К сожалению вопросы закончились':
        params = {'form': {
            'title': title
        }}
        return render_template('bad.html', **params)
    else:
        img_this = img_vopr(title)
        form = AnswerForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            right_answer = session.query(Second_page).filter(Second_page.title == title).first()
            if right_answer.otve in form.answer.data.lower():
                k += 10
            session.commit()
            return redirect('/game')
        return render_template('animals.html', title=title, img_vopr=url_for('static', filename=img_this), form=form)


@app.route('/units', methods=['GET', 'POST'])
def units():
    global k
    title = obr_vop(4)
    if title == 'К сожалению вопросы закончились':
        params = {'form': {
            'title': title
        }}
        return render_template('bad.html', **params)
    else:
        img_this = img_vopr(title)
        form = AnswerForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            right_answer = session.query(Second_page).filter(Second_page.title == title).first()
            if right_answer.otve in form.answer.data.lower():
                k += 10
            session.commit()
            return redirect('/game')
        return render_template('units.html', title=title, img_vopr=url_for('static', filename=img_this), form=form)


@app.route('/hodgepodge', methods=['GET', 'POST'])
def hodgepodge():
    global k
    title = obr_vop(5)
    if title == 'К сожалению вопросы закончились':
        params = {'form':{
            'title': title
        }}
        return render_template('bad.html', **params)
    else:
        img_this = img_vopr(title)
        form = AnswerForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            right_answer = session.query(Second_page).filter(Second_page.title == title).first()
            print(title)
            print(right_answer.otve)
            if right_answer.otve in form.answer.data.lower():
                k += 10
            session.commit()
            return redirect('/game')
        return render_template('hodgepodge.html', title=title, img_vopr=url_for('static', filename=img_this), form=form)


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
    if len(result) == 0:
        return 'К сожалению вопросы закончились'
    else:
        vopr_ud = session.query(Second_page).filter(Second_page.id == result[a].id).first()
        vopr_ud.kol_isp = 1
    session.commit()
    return result[a].title


def name_vopr():
    session = db_session.create_session()
    result = []
    for i in session.query(First_page).all():
        result.append(i.tema_vopr)
    return result


def img_vopr(title):
    session = db_session.create_session()
    result = session.query(Second_page).filter(Second_page.title == title).first()
    return result.img


def right_answer(title):
    session = db_session.create_session()
    result = session.query(Second_page).filter(Second_page.title == title).first()
    return result.otve


class AnswerForm(FlaskForm):
    answer = TextAreaField("Ответ: ")
    submit = SubmitField('Отправить')


if __name__ == '__main__':
    db_session.global_init("db/game.sqlite")
    app.run(port=8080, host='127.0.0.1')