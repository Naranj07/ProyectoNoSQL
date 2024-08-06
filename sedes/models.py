from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid



class Sede:


  def add_sede(self):

    # Crear sede
    sede = {
      "_id": uuid.uuid4().hex,
      "id_sede": request.form.get('id_sede'),
      "provincia": request.form.get('provincia'),
      "direccion": request.form.get('direccion'),
      "horario": request.form.get('horario'),
      "clases":request.form.get('clases')
    }


    if db.Sedes.find_one({ "id_sede": sede['id_sede'] }):
      return jsonify({ "error": "La sede ya existe" }), 400

    db.Sedes.insert_one(sede)

    return redirect(url_for('sede_view'))



    # Eliminar sede
  def delete_sede(self, sede_id):
        result = db.sedes.delete_one({"id_sede": sede_id})
        if result.deleted_count == 1:
            return redirect(url_for('sede_view')) # Redirige a la página de sede después de la eliminación
        else:
            return jsonify({"error": "La sede no fue encontrada"}), 404
        


    # Editar sede
  def edit_sede(self, sede_id):
        updated_sede = {
            "id_sede": request.form.get('id_sede'),
            "provincia": request.form.get('provincia'),
            "direccion": request.form.get('direccion'),
            "horario": request.form.get('horario'),
            "clases":request.form.get('clases')
        }

        result = db.Sedes.update_one({"id_sede":  sede_id}, {"$set": updated_sede})
        if result.modified_count == 1:
            return redirect(url_for('sede_view'))
        else:
            return jsonify({"error": "La sede no fue encontrada o no se hicieron cambios"}), 404