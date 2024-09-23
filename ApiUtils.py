import requests

# Mantener la función para obtener la hora local desde la API local
def obtener_hora_local():
    try:
        response = requests.get('http://127.0.0.1:5000/hora')
        if response.status_code == 200:
            return response.json().get('hora', 'Hora no disponible')
        else:
            return f"Error al obtener la hora: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

# Extraer la IP desde MockAPI
def obtener_ip_desde_mockapi():
    try:
        response = requests.get('https://66eb01a455ad32cda47b4d0a.mockapi.io/IoTCarStatus')
        if response.status_code == 200:
            # Tomar el último registro disponible
            registros = response.json()
            if registros:
                return registros[-1].get('ipClient', 'IP no disponible')
            else:
                return 'No hay registros disponibles para obtener la IP'
        else:
            return f"Error al obtener la IP: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

# Funciones
def inyectar_accion(accion):
    data = {
        "accion": accion

    }
    try:
        response = requests.post('https://66eb01a455ad32cda47b4d0a.mockapi.io/IoTCarStatus', json=data)
        if response.status_code == 201:
            return "Acción inyectada correctamente"
        else:
            return f"Error al inyectar la acción: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

def obtener_historial():
    try:
        response = requests.get('https://66eb01a455ad32cda47b4d0a.mockapi.io/IoTCarStatus')
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error al obtener el historial: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"
