from flask import Flask
from app import app
from sedes.models import Sede

@app.route('/sede/add_sede', methods=['GET','POST'])
def add_sede():
  return Sede().add_sede()

@app.route('/sede/delete_sede/<sede_id>', methods=['GET'])
def delete_sede(sede_id):
    return Sede().delete_sede(sede_id)


@app.route('/sede/edit_sede/<sede_id>', methods=['POST'])
def edit_sede(sede_id):
    return Sede().edit_sede(sede_id)
