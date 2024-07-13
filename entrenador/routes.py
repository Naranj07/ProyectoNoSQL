from flask import Flask
from app import app
from entrenador.models import Entrenador

@app.route('/entrenador/add_trainer', methods=['POST'])
def add_trainer():
  return Entrenador().add_trainer()

@app.route('/entrenador/delete_trainer/<trainer_id>', methods=['GET'])
def delete_trainer(trainer_id):
    return Entrenador().delete_trainer(trainer_id)


@app.route('/entrenador/edit_trainer/<trainer_id>', methods=['POST'])
def edit_trainer(trainer_id):
    return Entrenador().edit_trainer(trainer_id)