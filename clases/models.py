from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid



class Clases:


  def add_clases(self):

    # Crear Clases
    Clases = {
      "_id": uuid.uuid4().hex,
      "nombre": request.form.get('nombre'),
      "idEntrenador": request.form.get('idEntrenador'),
      "horario": request.form.get('horario'),
      "maxParticipantes": request.form.get('maxParticipantes'),
    }


    if db.Clases.find_one({ "_id": Clases['_id'] }):
      return jsonify({ "error": "La Clases ya existe" }), 400

    db.Clases.insert_one(Clases)

    return redirect(url_for('clases_view'))



    # Eliminar Clase
  def delete_clases(self, _id):
        result = db.Clases.delete_one({"_id": _id})
        if result.deleted_count == 1:
            return redirect(url_for('clases_view')) # Redirige a la página de Clase después de la eliminación
        else:
            return jsonify({"error": "La Clases no fue encontrado"}), 404
        


    # Editar Clase
  def edit_clases(self, _id):
        updated_clase = {
            "_id": request.form.get('_id'),
            "_nombre": request.form.get('nombre'),
            "idEntrenador": request.form.get('idEntrnador'),
            "horario": request.form.get('horario'),
            "maxParticpantes": request.form.get('maxParticpantes')
        }

        result = db.Clases.update_one({"_id":  _id}, {"$set": updated_clase})
        if result.modified_count == 1:
            return redirect(url_for('clases_view'))
        else:
            return jsonify({"error": "La Clase no fue encontrada o no se hicieron cambios"}), 404