from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid



class Usuario:

  #Sesiones
  def start_session(self, user):
    del user['contrasena']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200


  def signup(self):

    # Crear Usuario
    user = {
      "_id": uuid.uuid4().hex,
      "cedula": request.form.get('cedula'),
      "correo": request.form.get('correo'),
      "contrasena": request.form.get('contrasena'),
      "Membresia_id": request.form.get('Membresia_id'),
      "Nombre_completo": request.form.get('Nombre_completo'),
      "Telefono": request.form.get('Telefono')
    }

    #encryptar contrasena
    user['contrasena'] = pbkdf2_sha256.encrypt(user['contrasena'])


    #Verificacion de email    
    if db.usuarios.find_one({ "correo": user['correo'] }):
      return jsonify({ "error": "El correo ya existe!!" }), 400
    
    #Se inserta y se inicia la sesion
    if db.usuarios.insert_one(user):
          return self.start_session(user)

    return jsonify({ "error": "Error al crear el usuario" }), 400
  

  #Deslogear
  def signout(self):
    session.clear()
    return redirect('/')
  

  #logearse
  def login(self):

    user = db.usuarios.find_one({
      "correo": request.form.get('correo')
    })

    if user and pbkdf2_sha256.verify(request.form.get('contrasena'), user['contrasena']):
      return self.start_session(user)
    
    return jsonify({ "error": "Las credenciales son incorrectas" }), 401