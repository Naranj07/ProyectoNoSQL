from flask import Flask
from app import app
from reservas.models import Reservas

@app.route('/reservas/add_reservas', methods=['POST'])
def add_reservas():
  return Reservas().add_reservas()

@app.route('/reservas/delete_reservas/<_id>', methods=['GET'])
def delete_reservas(_id):
    return Reservas().delete_reservas(_id)


@app.route('/reservas/edit_reservas/<_id>', methods=['POST'])
def edit_reservas(_id):
    return Reservas().edit_reservas(_id)