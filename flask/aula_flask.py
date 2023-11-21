 from flask import Flask #importação do Flask

app = Flask(__name__) #instância do Flask

@app.route("/") #sobresaindo a função route na função index
def index():
    return "Hello world!"

if __name__ == "__main__": #verificando se é  o arquivo principal que está sendo executado, e não o secundário  
    app.run()