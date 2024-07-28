from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid



class Membresia:


  def add_membresia(self):

    # Crear Membresia
    membresia = {
      "_id": uuid.uuid4().hex,
      "id_membresia": request.form.get('id_membresia'),
      "tipo_membresia": request.form.get('tipo_membresia'),
      "descripcion": request.form.get('descripcion'),
      "precio": request.form.get('precio'),
    }


    if db.Membresias.find_one({ "id_membresia": membresia['id_membresia'] }):
      return jsonify({ "error": "La membresia ya existe" }), 400

    db.Membresias.insert_one(membresia)

    return redirect(url_for('membresia_view'))



    # Eliminar Membresia
  def delete_membresia(self, membresia_id):
        result = db.Membresias.delete_one({"_id": membresia_id})
        if result.deleted_count == 1:
            return redirect(url_for('membresia_view')) # Redirige a la página de Membresia después de la eliminación
        else:
            return jsonify({"error": "El Membresia no fue encontrado"}), 404
        


    # Editar Membresia
  def edit_membresia(self, membresia_id):
        updated_membresia = {
            "id_membresia": request.form.get('id_membresia'),
            "tipo_membresia": request.form.get('tipo_membresia'),
            "descripcion": request.form.get('descripcion'),
            "precio": request.form.get('precio')
        }

        result = db.Membresias.update_one({"id_membresia":  membresia_id}, {"$set": updated_membresia})
        if result.modified_count == 1:
            return redirect(url_for('membresia_view'))
        else:
            return jsonify({"error": "La Membresia no fue encontrada o no se hicieron cambios"}), 404
  

  


