from flask import Flask 
app = Flask(__name__)  

@app.route("/")
def index():
    return "Hello,world!"

@app.route('/<usuario>')
def ruta(usuario):
    return('<p>Hello , {}.</p>',format(usuario))
