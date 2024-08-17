from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import db
import uuid



class Factura:


  def add_factura(self):


    # Crear Factura
    factura = {
      "_id": uuid.uuid4().hex,
      "usuario": request.form.get('Nombre_completo'),
      "detalle_factura": request.form.get('Membresia_nombre'),
       "pago": request.form.get('pago'),
       "fecha": request.form.get('fecha'),
       "metodo_de_pago": request.form.get('metodoPago')
     }
    
#    factura = {
#      "_id": uuid.uuid4().hex,
#      "id_factura": request.form.get('id_factura'),
#      "userId": request.form.get('userId'),
#      "detalle_factura": request.form.get('detalle_factura'),
#      "id_membresia": request.form.get('id_membresia'),
#      "fecha": request.form.get('fecha')
#    }


    if db.Facturas.find_one({ "_id": factura['_id'] }):
      return jsonify({ "error": "La factura ya existe" }), 400

    db.Facturas.insert_one(factura)

    return jsonify({ "success": "factura creada" }), 200



    # Eliminar Factura
  def delete_factura(self, factura_id):
        result = db.facturas.delete_one({"id_factura": factura_id})
        if result.deleted_count == 1:
            return redirect(url_for('view_facturas')) # Redirige a la página de factura después de la eliminación
        else:
            return jsonify({"error": "La factura no fue encontrada"}), 404
        


    # Editar factura
  def edit_factura(self, factura_id):
        updated_factura = {
            "id_factura": request.form.get('id_factura'),
            "userId": request.form.get('userId'),
            "detalle_factura": request.form.get('detalle_factura'),
            "id_membresia": request.form.get('id_membresia'),
            "fecha": request.form.get('fecha')
        }

        result = db.facturas.update_one({"id_factura":  factura_id}, {"$set": updated_factura})
        if result.modified_count == 1:
            return redirect(url_for('view_facturas'))
        else:
            return jsonify({"error": "La factura no fue encontrada o no se hicieron cambios"}), 404
  
