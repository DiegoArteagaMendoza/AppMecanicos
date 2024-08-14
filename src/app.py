from flask import render_template, request, redirect, url_for
import json, os, random

def init_routes(app):

    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/Servicios')
    def servicios():
        return render_template("servicios.html")

    @app.route('/Clientes')
    def clientes():
        if os.path.exists('clients.json'):
            with open('clients.json', 'r') as file:
                clients = json.load(file)
            with open('vehiculos.json', 'r') as file:
                vehiculos = json.load(file)
        else:
            clients = []
            vehiculos = []
        
        return render_template("clientes.html", clients=clients, vehiculos=vehiculos)

    @app.route('/AgregarClientes')
    def formAddCliente():
        return render_template("addcliente.html")

    @app.route('/addCliente', methods=['POST'])
    def addCliente():
        id_cliente = random.random()
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        date = request.form['date']

        type = request.form['tipo']
        marca = request.form['marca']
        modelo = request.form['modelo']
        trabajo = request.form['OpcionesTrabajo']
        motivo = request.form['motivo']

        client = {
            "name": name,
            "phone": phone,
            "email": email,
            "date": date,
            "id": id_cliente
        }

        vehiculo = {
            "type": type,
            "marca": marca,
            "modelo": modelo,
            "OpcionesTrabajo": trabajo,
            "motivo": motivo,
            "id": id_cliente
        }

        if os.path.exists('clients.json'):
            with open('clients.json', 'r') as file:
                clients = json.load(file)
        else:
            clients = []

        if os.path.exists('vehiculos.json'):
            with open('vehiculos.json', 'r') as file:
                vehiculos = json.load(file)
        else:
            vehiculos = []
        
        clients.append(client)
        vehiculos.append(vehiculo)
        
        with open('clients.json', 'w') as file:
            json.dump(clients, file, indent=4)
        with open('vehiculos.json', 'w') as file:
            json.dump(vehiculos, file, indent=4)
        
        return redirect(url_for('clientes'))












# from flask import Flask, render_template, request, redirect, url_for
# import json, os, random

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/Servicios')
# def servicios():
#     return render_template("servicios.html")

# @app.route('/Clientes')
# def clientes():
#     if os.path.exists('clients.json'):
#         with open('clients.json', 'r') as file:
#             clients = json.load(file)
#         with open('vehiculos.json', 'r') as file:
#             vehiculos = json.load(file)
#     else:
#         clients = []
#         vehiculos = []
    
#     print(clients)
#     print(vehiculos)

#     return render_template("clientes.html", clients=clients, vehiculos=vehiculos)


# @app.route('/AgregarClientes')
# def formAddCliente():
#     return render_template("addcliente.html")

# @app.route('/addCliente', methods=['POST'])
# def addCliente():
#     id_cliente = random.random()
#     name = request.form['name']
#     phone = request.form['phone']
#     email = request.form['email']
#     date = request.form['date']

#     type = request.form['tipo']
#     marca = request.form['marca']
#     modelo = request.form['modelo']
#     trabajo = request.form['OpcionesTrabajo']
#     motivo = request.form['motivo']

#     # crear diccionario para el posterior json
#     client = {
#         "name": name,
#         "phone": phone,
#         "email": email,
#         "date": date,
#         "id": id_cliente
#     }

#     vehiculo = {
#         "type": type,
#         "marca": marca,
#         "modelo": modelo,
#         "OpcionesTrabajo": trabajo,
#         "motivo": motivo,
#         "id": id_cliente
#     }

#     # Leer el archivo JSON existente o crear uno nuevo si no existe
#     if os.path.exists('clients.json'):
#         with open('clients.json', 'r') as file:
#             clients = json.load(file)
#     else:
#         clients = []

#     if os.path.exists('vehiculos.json'):
#         with open('vehiculos.json', 'r') as file:
#             vehiculos = json.load(file)
#     else:
#         vehiculos = []
    
#     # Agregar el nuevo cliente a la lista
#     clients.append(client)
#     vehiculos.append(vehiculo)
    
#     # Guardar la lista actualizada en el archivo JSON
#     with open('clients.json', 'w') as file:
#         json.dump(clients, file, indent=4)
#     with open('vehiculos.json', 'w') as file:
#         json.dump(vehiculos, file, indent=4)
    
#     # Redirigir de vuelta al formulario para limpiarlo
#     return redirect(url_for('clientes'))

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=4000, debug=True)