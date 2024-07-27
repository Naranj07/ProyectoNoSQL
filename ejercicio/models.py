from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
import re

class Ejercicio:


  def add_exercise(self):

    # Crear Ejercicio
    exercise = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "description": request.form.get('description'),
      "youtubeLink": request.form.get('youtubeLink')
    }

    if db.Ejercicios.find_one({ "name": exercise['name'] }):
      return jsonify({ "error": "Este ejercicio ya existe" }), 400

    db.Ejercicios.insert_one(exercise)

    return jsonify(exercise), 200
  


    # Eliminar Ejercicio

  def delete_exercise(self, exercise_id):
        result = db.Ejercicios.delete_one({"_id": exercise_id})
        if result.deleted_count == 1:
            return redirect(url_for('ejercicio_view'))  # Redirige a la página de ejercicios después de la eliminación
        else:
            return jsonify({"error": "El ejercicio no fue encontrado"}), 404
        



    # Editar Entrenador
  def edit_exercise(self, exercise_id):
        updated_exercise = {
            "name": request.form.get('name'),
            "description": request.form.get('description'),
            "youtubeLink": request.form.get('youtubeLink')
        }

        result = db.Ejercicios.update_one({"_id": exercise_id}, {"$set": updated_exercise})
        if result.modified_count == 1:
            return redirect(url_for('ejercicio_view'))
        else:
            return jsonify({"error": "El ejercicio no fue encontrado o no se hicieron cambios"}), 404


