import tkinter as tk
from ApiUtils import inyectar_accion, obtener_hora_local, obtener_ip_desde_mockapi, obtener_historial


class IoTCarStatusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Car Status App")

        # Crear los botones de dirección
        self.crear_controles()

        # Crear área de historial
        self.historial_area = tk.Text(root, height=10, width=50)
        self.historial_area.grid(row=6, column=0, columnspan=3)

        # Mostrar la hora y la IP iniciales
        self.mostrar_hora_ip()

    def crear_controles(self):
        # Colocar los botones en la cuadrícula
        self.boton_arriba = tk.Button(self.root, text="Arriba", command=lambda: self.enviar_accion("Arriba"))
        self.boton_arriba.grid(row=0, column=1)  # Botón Arriba en el centro de la fila 0

        self.boton_abajo = tk.Button(self.root, text="Abajo", command=lambda: self.enviar_accion("Abajo"))
        self.boton_abajo.grid(row=2, column=1)  # Botón Abajo en el centro de la fila 2

        self.boton_izquierda = tk.Button(self.root, text="Izquierda", command=lambda: self.enviar_accion("Izquierda"))
        self.boton_izquierda.grid(row=1, column=0)  # Botón Izquierda en la fila 1, columna 0

        self.boton_derecha = tk.Button(self.root, text="Derecha", command=lambda: self.enviar_accion("Derecha"))
        self.boton_derecha.grid(row=1, column=2)  # Botón Derecha en la fila 1, columna 2

        # Colocar el botón STOP en el centro (fila 1, columna 1)
        self.boton_stop = tk.Button(self.root, text="STOP", command=lambda: self.enviar_accion("STOP"))
        self.boton_stop.grid(row=1, column=1)  # Botón STOP en el centro

        # Botón de Historial en una fila inferior
        self.boton_historial = tk.Button(self.root, text="Historial", command=self.mostrar_historial)
        self.boton_historial.grid(row=7, column=1)

    def mostrar_hora_ip(self):
        hora = obtener_hora_local()
        ip = obtener_ip_desde_mockapi()

        # Crear o actualizar etiquetas
        if not hasattr(self, 'etiqueta_hora'):
            self.etiqueta_hora = tk.Label(self.root, text=f"Hora: {hora}")
            self.etiqueta_hora.grid(row=3, column=1)
        else:
            self.etiqueta_hora.config(text=f"Hora: {hora}")

        if not hasattr(self, 'etiqueta_ip'):
            self.etiqueta_ip = tk.Label(self.root, text=f"IP: {ip}")
            self.etiqueta_ip.grid(row=4, column=1)
        else:
            self.etiqueta_ip.config(text=f"IP: {ip}")

        # Actualizar cada 10 segundos
        self.root.after(10000, self.mostrar_hora_ip)

    def enviar_accion(self, accion):
        resultado = inyectar_accion(accion)
        self.historial_area.insert(tk.END, f"{accion}: {resultado}\n")

    def mostrar_historial(self):
        historial = obtener_historial()
        if isinstance(historial, list):
            self.historial_area.delete(1.0, tk.END)  # Limpiar el área
            ultimos_10 = historial[-10:]  # Obtener los últimos 10 registros
            for i, registro in enumerate(ultimos_10):
                self.historial_area.insert(tk.END,
                                           f"{i + 1}. ID: {registro['id']}, Acción: {registro['accion']}, Fecha: {registro['date']}\n")
            if ultimos_10:
                self.historial_area.insert(tk.END,
                                           f"**ÚLTIMO MOVIMIENTO** - ID: {ultimos_10[-1]['id']}, Acción: {ultimos_10[-1]['accion']}, Fecha: {ultimos_10[-1]['date']}\n")
        else:
            self.historial_area.insert(tk.END, historial + "\n")
