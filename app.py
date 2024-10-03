from flask import (Flask, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): #função responsável pela página
    nome = request.args.get('nome') #use o seu nome
    # HTML retornado
    return f"""<h1>Página inicial</h1>
    <p>Olá {nome}, que nome bonito!
  """      

@app.route("/galeria", methods=('GET',))
def outra():
    return "<h1>galeria</h1>"

@app.route("/contato", methods=('GET',))
def outra1():
    return "<h1>contato</h1>"

@app.route("/sobre", methods=('GET',))
def outra2():
    return "<h1>sobre</h1>"