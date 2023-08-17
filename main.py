from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def homepage():
    return render_template('homepage.html')


@app.route('/imobiliaria')
def imobiliaria():
    return render_template('imobiliaria.html')


@app.route('/padaria')
def padaria():
    return render_template('padaria.html')


if __name__ == '__main__':
    app.run()
