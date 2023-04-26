from flask import Flask, render_template
from mongoengine import connect, Document, StringField, DateTimeField, ListField

# Conecta ao banco de dados MongoDB hospedado no Atlas
connect(host='mongodb+srv://pedropaulo:victor12@cluster0.jscxnyc.mongodb.net/test')




# Cria uma instância do aplicativo Flask
app = Flask(__name__)

# Define as rotas do aplicativo
@app.route("/")
def index():
    return render_template("template.html",tarefa = "Teste")

@app.route("/principal")
def principal():
    #class Projeto(Document):
     #   nome_do_projeto = StringField(required=True)
      #  data_de_entrega = DateTimeField(required=True)
       # lider = StringField(required=True)
        #integrantes = ListField(StringField())

    #projeto = Projeto(nome_do_projeto='Projeto A', data_de_entrega='2023-12-31', lider='João', integrantes=['Maria', 'Pedro'])
    #projeto.save()

    return render_template("principal.html")

@app.route("/cadastrar/projeto")
def cadastrar():
    return render_template("create.html")

@app.route("/projeto")
def projeto():
    return render_template("project.html")

@app.route("/cadastrar/tarefa")
def cadastrarTarefa():
    return render_template("createTarefa.html")

# Cria um novo projeto e o salva no banco de dados


# Inicia o servidor Flask
if __name__ == "__main__":
    app.run()
