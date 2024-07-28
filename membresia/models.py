from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid



class Membresias:


  def add_membresia(self):

    # Crear Membresias
    membresia = {
      "_id": uuid.uuid4().hex,
      "fullName": request.form.get('fullName'),
      "specialization": request.form.get('specialization'),
      "phoneNumber": request.form.get('contrasena'),
      "contactDetails": {
                "phoneNumber": request.form.get('phoneNumber'),
                "email": request.form.get('email')
            }
    }


    if db.membresias.find_one({ "fullName": membresia['fullName'] }):
      return jsonify({ "error": "El entranador ya existe" }), 400

    db.membresias.insert_one(membresia)

    return jsonify(membresia), 200
  


    # Eliminar Membresias
  def delete_membresia(self, membresia_id):
        result = db.membresias.delete_one({"_id": membresia_id})
        if result.deleted_count == 1:
            return redirect(url_for('Membresias_view'))  # Redirige a la página de membresias después de la eliminación
        else:
            return jsonify({"error": "El Membresias no fue encontrado"}), 404




    # Editar Membresias
  def edit_membresia(self, membresia_id):
        updated_membresia = {
            "fullName": request.form.get('fullName'),
            "specialization": request.form.get('specialization'),
            "phoneNumber": request.form.get('phoneNumber'),
            "contactDetails": {
                "email": request.form.get('email')
            }
        }

        result = db.membresias.update_one({"_id": membresia_id}, {"$set": updated_membresia})
        if result.modified_count == 1:
            return redirect(url_for('Membresias_view'))
        else:
            return jsonify({"error": "El Membresias no fue encontrado o no se hicieron cambios"}), 404
  

  


