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