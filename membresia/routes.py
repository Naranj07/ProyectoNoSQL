from flask import Flask
from app import app
from membresia.models import Membresia

@app.route('/membresia/add_membresia', methods=['POST'])
def add_membresia():
  return Membresia().add_membresia()

@app.route('/membresia/delete_membresia/<membresia_id>', methods=['GET'])
def delete_membresia(membresia_id):
    return Membresia().delete_membresia(membresia_id)


@app.route('/membresia/edit_membresia/<membresia_id>', methods=['POST'])
def edit_membresia(membresia_id):
    return Membresia().edit_membresia(membresia_id)