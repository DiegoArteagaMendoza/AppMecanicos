from . import cargado, busqueda
import json


def guardar_datos_cliente_vehiculo(client, vehiculo, rut):
    clients, vehiculos, _, _, clientsUnico = cargado.cargar_datos()

    print(rut)

    clients.append(client)
    vehiculos.append(vehiculo)

    if rut:
        if busqueda.buscarCliente(rut):
            print(" ")
        else:
            client_sin_idTrabajo = {key: value for key, value in client.items() if key != 'idTrabajo'}
            clientsUnico.append(client_sin_idTrabajo)
            with open('clientesUnico.json', 'w') as file:
                json.dump(clientsUnico, file, indent=4)

    with open('clients.json', 'w') as file:
        json.dump(clients, file, indent=4)

    with open('vehiculos.json', 'w') as file:
        json.dump(vehiculos, file, indent=4)

def guardar_servicio(servicio, imagen):
    _, _, servicios, imagenes, _ = cargado.cargar_datos()
    
    servicios.append(servicio)
    imagenes.append(imagen)

    with open('servicios.json', 'w') as file:
        json.dump(servicios, file, indent=4)
    
    with open('imagenes.json', 'w') as file:
        json.dump(imagenes, file, indent=4)