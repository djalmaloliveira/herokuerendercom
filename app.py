import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return '<h1>Ola, Mundo3</h1>'\

@app.route('/usuario')
def usuario():
    return '<h1>Você usuário seja bem vindo</h1>'

@app.route('/teste')
def teste():
    return '<h1>Pagina teste</h1>'
