import requests
from datetime import datetime
import json

BASE_URL = 'https://66eb01a455ad32cda47b4d0a.mockapi.io/IoTCarStatus'

# Función para obtener la hora desde la API local
def obtener_hora_local():
    try:
        response = requests.get('http://127.0.0.1:5000/hora')
        if response.status_code == 200:
            return response.json().get('hora', 'Error al obtener la hora')
        else:
            return 'Error al conectar con la API local'
    except requests.RequestException as e:
        return f'Error: {e}'

# Función para obtener la IP del cliente desde la API local
def obtener_ip_cliente():
    try:
        response = requests.get('http://127.0.0.1:5000/ip')
        if response.status_code == 200:
            return response.json().get('ip', 'Error al obtener la IP')
        else:
            return 'Error al conectar con la API local'
    except requests.RequestException as e:
        return f'Error: {e}'

# Función para inyectar acción en MockAPI, incluyendo hora y IP cliente
def inyectar_accion(accion):
    try:
        # Obtener hora actual desde la API local
        hora_actual = obtener_hora_local()
        ip_cliente = obtener_ip_cliente()

        # Si falla, usar la hora del sistema como fallback
        if 'Error' in hora_actual:
            hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Obtener solo la fecha en formato Año-Mes-Día
        fecha_actual = hora_actual.split(' ')[0]

        # Estructura de los datos a enviar
        data = {
            "accion": accion,
            "ipClient": ip_cliente,
            "date": fecha_actual
        }

        # Realizar la petición POST a MockAPI
        response = requests.post(BASE_URL, json=data)
        if response.status_code == 201:
            return "Acción inyectada correctamente"
        else:
            return f"Error al inyectar la acción: {response.status_code}"
    except requests.RequestException as e:
        return f'Error: {e}'

# Función para obtener el historial (últimos 10 registros de MockAPI)
def obtener_historial():
    try:
        # Solicitar los últimos 10 registros ordenados por fecha de creación (desc)
        response = requests.get(f"{BASE_URL}?limit=10&sortBy=createdAt&order=desc")
        if response.status_code == 200:
            return response.json()  # Devolver los registros como lista de diccionarios
        else:
            return f"Error al obtener el historial: {response.status_code}"
    except requests.RequestException as e:
        return f"Error: {e}"

