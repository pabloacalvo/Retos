from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Aplicar CORS solo a una ruta especifica
"""
Solo va permitir origenes de localhost y metodos GET y POST y en el headers debe contener el Content-Type 
"""
CORS(app, resources = {r"/api/":{
    "origins":["localhost:3000", "0.0.0.0:3000"],
    "methods":["GET","POST"],
    "allow_headers":["Content-Type"]
}})

"""
# Ejemplo todos los origenes
CORS(app, resources = {r"/*":{
    "origins":"*",
    "methods":["GET","POST"],
    "allow_headers":["Content-Type"]
}})
"""


@app.route('/')
def hello_world():
    return "Hola mundo"

@app.route('/api/data')
def api_data():
    return "Datos de la API"

if __name__ == "__main__":
    app.run()