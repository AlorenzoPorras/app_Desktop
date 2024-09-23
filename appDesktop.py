import tkinter as tk
from IoTCarStatusApp import IoTCarStatusApp
import threading
from flask import Flask, jsonify
from datetime import datetime

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para obtener la hora actual
@app.route('/hora', methods=['GET'])
def obtener_hora():
    hora_actual = datetime.now().strftime('%H:%M:%S')
    return jsonify({"hora": hora_actual})

# Función para iniciar el servidor Flask en un hilo separado
def iniciar_servidor():
    app.run(port=5000)

if __name__ == "__main__":
    # Inicia el servidor Flask en un hilo separado
    servidor_thread = threading.Thread(target=iniciar_servidor)
    servidor_thread.daemon = True  # El hilo termina cuando la aplicación principal se cierra
    servidor_thread.start()

    # Inicia la aplicación Tkinter
    root = tk.Tk()
    app = IoTCarStatusApp(root)
    root.mainloop()
