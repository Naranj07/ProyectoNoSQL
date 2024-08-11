from flask import Flask
from app import app
from ejercicio.models import Ejercicio

@app.route('/ejercicio/add_exercise', methods=['GET','POST'])
def add_exercise():
  return Ejercicio().add_exercise()

@app.route('/ejercicio/delete_exercise/<exercise_id>', methods=['GET'])
def delete_exercise(exercise_id):
    return Ejercicio().delete_exercise(exercise_id)


@app.route('/ejercicio/edit_exercise/<exercise_id>', methods=['POST'])
def edit_exercise(exercise_id):
    return Ejercicio().edit_exercise(exercise_id)