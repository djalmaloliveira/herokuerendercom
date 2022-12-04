from flask import Flask

app = Flask(__name__)


@app.get('/')
def index():
    return 'app renderizado'


@app.get('/inscrito/<nome_inscrito>')
def inscrito(nome_inscrito):
    return f'Ola {nome_inscrito}'


if __name__ == '__main__':
    app.run(debug=True)
