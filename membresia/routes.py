from flask import Flask
from app import app
from membresias.models import membresias

@app.route('/membresias/add_trainer', methods=['POST'])
def add_trainer():
  return membresias().add_trainer()

@app.route('/membresias/delete_trainer/<trainer_id>', methods=['GET'])
def delete_trainer(trainer_id):
    return membresias().delete_trainer(trainer_id)


@app.route('/membresias/edit_trainer/<trainer_id>', methods=['POST'])
def edit_trainer(trainer_id):
    return membresias().edit_trainer(trainer_id)