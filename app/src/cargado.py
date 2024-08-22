import json, os

def cargar_datos():
        if os.path.exists('clients.json'):
            with open('clients.json', 'r') as file:
                clients = json.load(file)
        else:
            clients = []

        if os.path.exists('clientesUnico.json'):
            with open('clientesUnico.json', 'r') as file:
                clientsUnico = json.load(file)
        else:
            clientsUnico = []

        if os.path.exists('vehiculos.json'):
            with open('vehiculos.json', 'r') as file:
                vehiculos = json.load(file)
        else:
            vehiculos = []

        if os.path.exists('servicios.json'):
            with open('servicios.json', 'r') as file:
                servicios = json.load(file)
        else:
            servicios = []

        if os.path.exists('imagenes.json'):
            with open('imagenes.json', 'r') as file:
                imagenes = json.load(file)
        else:
            imagenes = []

        return clients, vehiculos, servicios, imagenes, clientsUnico