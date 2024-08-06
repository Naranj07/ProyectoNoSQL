from flask import Flask
from app import app
from facturas.models import Factura

@app.route('/factura/add_factura', methods=['POST'])
def add_factura():
  return Factura().add_factura()

@app.route('/factura/delete_factura/<factura_id>', methods=['GET'])
def delete_factura(factura_id):
    return Factura().delete_factura(factura_id)


@app.route('/factura/edit_factura/<factura_id>', methods=['POST'])
def edit_factura(factura_id):
    return Factura().edit_factura(factura_id)
  
