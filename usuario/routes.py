from flask import Flask
from app import app
from usuario.models import Usuario

@app.route('/usuario/signup', methods=['POST'])
def signup():
  return Usuario().signup()

@app.route('/usuario/signout')
def signout():
  return Usuario().signout()

@app.route('/usuario/login', methods=['POST'])
def usuario_login():
  return Usuario().login()