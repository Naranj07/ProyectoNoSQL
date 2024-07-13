from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid



class Entrenador:


  def add_trainer(self):

    # Crear Entrenador
    trainer = {
      "_id": uuid.uuid4().hex,
      "fullName": request.form.get('fullName'),
      "specialization": request.form.get('specialization'),
      "phoneNumber": request.form.get('contrasena'),
      "contactDetails": {
                "phoneNumber": request.form.get('phoneNumber'),
                "email": request.form.get('email')
            }
    }


    if db.Entrenadores.find_one({ "fullName": trainer['fullName'] }):
      return jsonify({ "error": "El entranador ya existe" }), 400

    db.Entrenadores.insert_one(trainer)

    return jsonify(trainer), 200
  


    # Eliminar Entrenador
  def delete_trainer(self, trainer_id):
        result = db.Entrenadores.delete_one({"_id": trainer_id})
        if result.deleted_count == 1:
            return redirect(url_for('entrenador_view'))  # Redirige a la página de entrenadores después de la eliminación
        else:
            return jsonify({"error": "El entrenador no fue encontrado"}), 404




    # Editar Entrenador
  def edit_trainer(self, trainer_id):
        updated_trainer = {
            "fullName": request.form.get('fullName'),
            "specialization": request.form.get('specialization'),
            "phoneNumber": request.form.get('phoneNumber'),
            "contactDetails": {
                "email": request.form.get('email')
            }
        }

        result = db.Entrenadores.update_one({"_id": trainer_id}, {"$set": updated_trainer})
        if result.modified_count == 1:
            return redirect(url_for('entrenador_view'))
        else:
            return jsonify({"error": "El entrenador no fue encontrado o no se hicieron cambios"}), 404
  

  


