from pymongo import MongoClient
import base64
from pathlib import Path

root = Path(__file__).parent
file = root/"imagen1.jpg"



# Función para leer y codificar la imagen en base64
def convertir_imagen_a_base64(ruta_imagen):
    with open(ruta_imagen, "rb") as imagen:
        imagen_codificada = base64.b64encode(imagen.read())
        return imagen_codificada.decode('utf-8')  # Para guardar como string
    
def iniciar():

    try:
        client = MongoClient('localhost', 27017)
        database = client['project1_python']
        collections = database['project1']
        image_transform = convertir_imagen_a_base64(file)
        #documents = collections.find()

        #Insertar un registro
        #collections.insert_one({"name":"Ruby","developers":500,"enabled":True})

        
        one = {"name":"C","developers":0,"enabled":False}
        two = {"name":"C++","developers":5,"enabled":True}
        document = {"name":"Imagen 1","imagen_base64":image_transform}
        #collections.insert_one(document)
        #Insertar varios registros
        #collections.insert_many([one,two])

        # Obtener resultados en formato cursor
        #result = collections.find()
        #for r in result:
            #print(r['name'])
        #Obtener resultados por parametros
        result2 = collections.find({'imagen_base64':'Imagen 1'})
        for r in result2:
            print(r)

    except Exception as e:
        print(e)
    finally:
        client.close()
        print('Conexion finalizada')

iniciar()