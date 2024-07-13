from flask import Flask, render_template, session, redirect, url_for
from functools import wraps

#se importa la base de datos
import database as dbase 

#con esto se conectara a la funcion para conectarse a la BD, dbase como se le llamo y su metodo dbConnection
db = dbase.dbConnection()

app = Flask(__name__)

#este es el key para la sesion
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'


# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap




#Rutas Usuario
from usuario import routes


@app.route('/')
def login_view():
    return render_template('login.html')


@app.route('/home/')
#intercepta la sesion
@login_required
def dashboard():
    return render_template('home.html')



#Rutas Entrenadores
from entrenador import routes

@app.route('/entrenador/')
def entrenador_view():
    entrenadores = db.Entrenadores.find()
    return render_template('entrenador.html', entrenadores=entrenadores)


