import requests
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

# Función para inyectar acciones en MockAPI
def inyectar_accion(accion):
    try:
        data = {"accion": accion}
        response = requests.post(BASE_URL, json=data)
        if response.status_code == 201:
            return "Acción inyectada correctamente"
        else:
            return "Error al inyectar la acción"
    except requests.RequestException as e:
        return f'Error: {e}'

# Función para obtener el historial (últimos 10 registros)
def obtener_historial():
    try:
        response = requests.get(BASE_URL + '?limit=10&sortBy=createdAt&order=desc')
        if response.status_code == 200:
            return response.json()
        else:
            return 'Error al obtener el historial'
    except requests.RequestException as e:
        return f'Error: {e}'
