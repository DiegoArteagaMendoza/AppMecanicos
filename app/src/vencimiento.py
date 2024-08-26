from datetime import datetime
from . import busqueda

def verVencimiento(rut, nservicio):
    # Buscar la fecha de ingreso y duración del servicio
    fechaIngreso = busqueda.buscarIngresoCliente(rut, nservicio)
    if fechaIngreso:
        tipoTrabajo = busqueda.buscarServicioCliente(rut, nservicio)
        tiempoTrabajo = busqueda.buscarTiempoServicio(tipoTrabajo)
        
        # Ajustar el formato de la fecha a '%Y-%m-%d' (año-mes-día)
        try:
            fechaInicio = datetime.strptime(fechaIngreso, "%Y-%m-%d")
        except ValueError:
            print(f"Formato de fecha inválido: {fechaIngreso}")
            return {"dias_atraso": -1, "dias_restantes": None}
        
        fechaActual = datetime.now()
        diferenciaDias = (fechaActual - fechaInicio).days
        tiempoTrabajo = int(tiempoTrabajo)

        # Calcular días de atraso y días restantes
        if diferenciaDias >= tiempoTrabajo:
            dias_atraso = diferenciaDias - tiempoTrabajo
            return {"dias_atraso": dias_atraso, "dias_restantes": 0}
        else:
            dias_restantes = tiempoTrabajo - diferenciaDias
            return {"dias_atraso": 0, "dias_restantes": dias_restantes}

    return {"dias_atraso": -1, "dias_restantes": None}  # Retornar valores predeterminados si no se encuentra la fecha de ingreso
