from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid



class Reservas:


  def add_reservas(self):

    # Crear Reservas
    Reservas = {
      "_id": uuid.uuid4().hex,
      "idUsuario": request.form.get('idUsuario'),
      "tipo": request.form.get('tipo'),
      "detalleClase": request.form.get('detalleClase'),
    }


    if db.Reservaciones.find_one({ "_id": Reservas['_id'] }):
      return jsonify({ "error": "La reserva ya existe" }), 400

    db.Reservaciones.insert_one(Reservas)

    return redirect(url_for('reservas_view'))



    # Eliminar Reserva
  def delete_reservas(self, _id):
        result = db.Reservaciones.delete_one({"_id": _id})
        if result.deleted_count == 1:
            return redirect(url_for('reservas_view')) # Redirige a la página de Reserva después de la eliminación
        else:
            return jsonify({"error": "La Reserva no fue encontrado"}), 404
        


    # Editar Reserva
  def edit_reservas(self, _id):
        updated_reserva = {
            "_id": request.form.get('_id'),
            "idUsuario": request.form.get('idUsuario'),
            "tipo": request.form.get('tipo'),
            "detalleClase": request.form.get('detalleClase')
        }

        result = db.Reservaciones.update_one({"_id":  _id}, {"$set": updated_reserva})
        if result.modified_count == 1:
            return redirect(url_for('reservas_view'))
        else:
            return jsonify({"error": "La Reserva no fue encontrada o no se hicieron cambios"}), 404