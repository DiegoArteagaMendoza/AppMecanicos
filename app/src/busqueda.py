import os, json


def buscarCliente(rut):
    if not os.path.exists('clientesUnico.json'):
        print("El archivo clientesUnico.json no existe")
        return False
    
    with open('clientesUnico.json', 'r') as file:
        clientesUnico = json.load(file)
    
    for cliente in clientesUnico:
        if rut == cliente['rut']:
            print(f"Cliente encontrado: {rut}")
            return True
    
    print("No se encontró al cliente")
    return False

def buscarIngresoCliente(rut, nservicio):
    if not os.path.exists('clients.json'):
        print("El archivo clients.json no existe")
        return False
    
    with open('clients.json', 'r') as file:
        clients = json.load(file)
    
    for cliente in clients:
        if rut == cliente['rut']:
            if nservicio == cliente['idTrabajo']:
                print(f"Cliente encontrado: {rut}")
                return cliente['date']
        
    print("No se encontro al cliente")
    return False

def buscarServicioCliente(rut, nservicio):
    if not os.path.exists('clients.json'):
        print("El archivo clients.json no existe")
        return False
    
    with open('clients.json', 'r') as file:
        clients = json.load(file)
    
    with open('vehiculos.json', 'r') as file:
        vehiculos = json.load(file)
    
    for cliente in clients:
        for vehiculo in vehiculos:
            if buscarCliente(cliente['rut']):
                if cliente['idTrabajo'] == vehiculo['idTrabajo']:
                    return vehiculo['OpcionesTrabajo']
        
    print("No se encontro al cliente")
    return False

def buscarTiempoServicio(tipoTrabajo):
    with open('servicios.json', 'r') as file:
        servicios = json.load(file)

    for servicio in servicios:
        if tipoTrabajo == servicio['name']:
            return servicio['tiempo']