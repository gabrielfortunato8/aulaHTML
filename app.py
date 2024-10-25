from flask import (Flask, render_template, request) # Importa o flask

app = Flask(__name__) # cria uma instância

@app.route("/", methods=('GET',)) # Assina uma rota
def index(): #função responsável pela página
    nome = request.args.get('Gabriel') #use o seu nome
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

@app.route("/area/<float:largura>/<float:altura>", methods=( 'GET', ))
def area(largura: float, altura: float):
    return f"""<h1> A área informada >L={largura} * A={altura} => Area={largura*altura}</h1>"""

@app.route("/parimpar/<float:numero>", methods=('GET',))
def par_ou_impar(numero):
  if numero % 2 == 0:
    return f"O número {numero} é par."
  else:
    return f"O número {numero} é ímpar."
  
@app.route("/sobrenome/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomesobrenome(nome: str, sobrenome: str):
  return f"""<h1> sobrenome </h1>
  <p>{sobrenome},{nome}</p>"""

@app.route("/potencia/<float:numero>/<float:elevado>", methods=('GET',))
def potencia(numero: float, elevado: float):
    return f"""<h1>A potencia é> N={numero}* E={elevado} => Potencia={numero*elevado}</h1>"""

@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET", ))
def tabuada(numero = None):

  if 'numero' in request.args: 
      numero = int(request.args.get('numero'))
                                
  return render_template('tabuada.html', numero=numero)

@app.route("/calculo")
@app.route("/calculo/<numero>", methods=("GET", ))
def calculo(numero = None):
   
  if 'valor' in request.args:
     numero = int(request.args.get('numero'))

  return render_template('calculos juros.html', numero=numero)

@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        if email == 'aluno@senai.br' and senha == 'senai':
            return '<h1>Usuário logado com sucesso😁!</h1>'
        else:
            return '<h1>Email ou senha incorretos, tente novamente😔.</h1>'

    return render_template('login.html')

@app.route("/imc", methods=('GET', 'POST'))
def calcular_imc():
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            imc = peso / (altura ** 2)

            if imc < 18.5:
                classificacao = 'Magreza'
                grau_obesidade = 0
            elif 18.5 <= imc <= 24.9:
                classificacao = 'Normal'
                grau_obesidade = 0
            elif 25.0 <= imc <= 29.9:
                classificacao = 'Sobrepeso'
                grau_obesidade = 1
            elif 30.0 <= imc <= 39.9:
                classificacao = 'Obesidade'
                grau_obesidade = 2
            else:
                classificacao = 'Obesidade Grave'
                grau_obesidade = 3

            return f'''
                <h1>Seu IMC é: {imc:.2f}</h1>
                <h2>Classificação: {classificacao}</h2>
                <h2>Grau de Obesidade: {grau_obesidade}</h2>
            '''
        except ValueError:
            return '<h1>Erro: Por favor insira valores válidos para peso e altura.</h1>'
    
    return render_template('calculo imc.html')