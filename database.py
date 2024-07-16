#se importan las librerias de mongo
from pymongo import MongoClient
import certifi


#Se crea la variable para conectar al cluster de BD
MONGO_URI = 'mongodb+srv://admin:1234@gimnasio.tjhaopv.mongodb.net/'

#instancia para certifi
ca = certifi.where()

#funcion para conectarse a la BD
def dbConnection():
    try:
        #client conecta a la direccion de mongo con el certifi
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        
        #aqui se crea la base de datos en caso de que no exista una
        db = client["GYMBoost"]

    except ConnectionError:
        print('Error de conexion con la Base de datos')
    return db



#Pruebas
#mongodb+srv://naranj07:Gafesoto01@cluster0.zabgog3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0