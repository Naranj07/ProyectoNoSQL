from flask import Flask
from app import app
from clases.models import Clases

@app.route('/clases/add_clases', methods=['GET', 'POST'])
def add_clases():
  return Clases().add_clases()

@app.route('/clases/delete_clases/<_id>', methods=['GET'])
def delete_clases(_id):
    return Clases().delete_clases(_id)


@app.route('/clases/edit_clases/<_id>', methods=['POST'])
def edit_clases(_id):
    return Clases().edit_clases(_id)