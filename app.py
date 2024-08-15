from flask import Flask, render_template, session, redirect, url_for
from functools import wraps
import re

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


  # Video de Youtube
@app.template_filter('youtube_embed_id')
def youtube_embed_id(link):
    """
    Extracts the YouTube video ID from a URL.
    """
    pattern = r'(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)([^"&?/ ]{11})'
    match = re.search(pattern, link)
    if match:
        return match.group(1)
    return link  # Return the original link if not matched




#Rutas Usuario
from usuario import routes

@app.route('/index/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

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


@app.route('/entrenadores/')
def entrenadores_view():
    entrenadores = db.Entrenadores.find()
    return render_template('entrenadores.html', entrenadores=entrenadores)


#Rutas Ejercicios
from ejercicio import routes

@app.route('/ejercicio/')
def ejercicio_view():
    ejercicios = db.Ejercicios.find()
    return render_template('ejercicio.html', ejercicios=ejercicios)

@app.route('/ejercicios/')
def ejercicios_view():
    ejercicios = db.Ejercicios.find()
    return render_template('ejercicios.html', ejercicios=ejercicios)


#Rutas Membresia
from membresia import routes 

@app.route('/membresia/')
def membresia_view():
    membresias = db.Membresias.find()
    return render_template('membresia.html', membresias=membresias)


#Rutas Reservas
from reservas import routes

@app.route('/reservas/')
def reservas_view():
    reservaciones = db.Reservaciones.find()
    return render_template('reservas.html', reservas=reservaciones)

if __name__ == '__main__':
    app.run(debug=True)

#Rutas Clases
from clases import routes

@app.route('/clases/')
def clases_view():
    clases = db.Clases.find()
    return render_template('clases.html', clases=clases)


#Rutas Factura
from facturas import routes

@app.route('/facturas/')
def view_facturas():
    facturas = db.Facturas.find()
    return render_template('factura.html', facturas=facturas)

#Rutas Sedes
from sedes import routes

@app.route('/sedes/')
def factura_view():
    sedes = db.Sedes.find()
    return render_template('sede.html', sedes=sedes)

