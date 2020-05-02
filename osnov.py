from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/game', methods=['GET', 'POST'])
def login():
    params = {}
    return render_template('secur.html', **params)


@app.route('/success')
def success():
    params = {}
    return render_template('seccess.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')