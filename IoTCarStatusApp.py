import tkinter as tk
from ApiUtils import inyectar_accion, obtener_hora_local, obtener_ip_desde_mockapi, obtener_historial

class IoTCarStatusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Car Status App")

        # Crear los botones de dirección
        self.crear_controles()

        # Mostrar la hora y la IP iniciales
        self.mostrar_hora_ip()

    def crear_controles(self):
        self.boton_arriba = tk.Button(self.root, text="Arriba", command=lambda: self.enviar_accion("Arriba"))
        self.boton_arriba.grid(row=0, column=1)

        self.boton_abajo = tk.Button(self.root, text="Abajo", command=lambda: self.enviar_accion("Abajo"))
        self.boton_abajo.grid(row=2, column=1)

        self.boton_izquierda = tk.Button(self.root, text="Izquierda", command=lambda: self.enviar_accion("Izquierda"))
        self.boton_izquierda.grid(row=1, column=0)

        self.boton_derecha = tk.Button(self.root, text="Derecha", command=lambda: self.enviar_accion("Derecha"))
        self.boton_derecha.grid(row=1, column=2)

        # Botones adicionales para giros
        self.boton_90_izquierda = tk.Button(self.root, text="Girar 90° Izquierda", command=lambda: self.enviar_accion("Girar 90° Izquierda"))
        self.boton_90_izquierda.grid(row=3, column=0)

        self.boton_90_derecha = tk.Button(self.root, text="Girar 90° Derecha", command=lambda: self.enviar_accion("Girar 90° Derecha"))
        self.boton_90_derecha.grid(row=3, column=2)

        self.boton_180 = tk.Button(self.root, text="Girar 180°", command=lambda: self.enviar_accion("Girar 180°"))
        self.boton_180.grid(row=4, column=1)

        self.boton_stop = tk.Button(self.root, text="STOP", command=lambda: self.enviar_accion("STOP"))
        self.boton_stop.grid(row=2, column=1)

        self.boton_historial = tk.Button(self.root, text="Historial", command=self.abrir_historial)
        self.boton_historial.grid(row=5, column=1)

    def mostrar_hora_ip(self):
        hora = obtener_hora_local()
        ip = obtener_ip_desde_mockapi()

        # Crear o actualizar etiquetas
        if not hasattr(self, 'etiqueta_hora'):
            self.etiqueta_hora = tk.Label(self.root, text=f"Hora: {hora}")
            self.etiqueta_hora.grid(row=6, column=1)
        else:
            self.etiqueta_hora.config(text=f"Hora: {hora}")

        if not hasattr(self, 'etiqueta_ip'):
            self.etiqueta_ip = tk.Label(self.root, text=f"IP: {ip}")
            self.etiqueta_ip.grid(row=7, column=1)
        else:
            self.etiqueta_ip.config(text=f"IP: {ip}")

        # Actualizar cada 10 segundos
        self.root.after(10000, self.mostrar_hora_ip)

    def enviar_accion(self, accion):
        resultado = inyectar_accion(accion)
        print(f"{accion}: {resultado}")  # Se puede mostrar en consola o un log si es necesario

    def abrir_historial(self):
        # Crear nueva ventana
        historial_ventana = tk.Toplevel(self.root)
        historial_ventana.title("Historial de Movimientos")

        historial_area = tk.Text(historial_ventana, height=10, width=50)
        historial_area.pack()

        historial = obtener_historial()
        if isinstance(historial, list):
            ultimos_10 = historial[-10:]  # Obtener los últimos 10 registros
            for i, registro in enumerate(ultimos_10):
                historial_area.insert(tk.END,
                                       f"{i + 1}. ID: {registro['id']}, Acción: {registro['accion']}, Fecha: {registro['date']}\n")
            if ultimos_10:
                historial_area.insert(tk.END,
                                       f"**ÚLTIMO MOVIMIENTO** - ID: {ultimos_10[-1]['id']}, Acción: {ultimos_10[-1]['accion']}, Fecha: {ultimos_10[-1]['date']}\n")
        else:
            historial_area.insert(tk.END, historial + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = IoTCarStatusApp(root)
    root.mainloop()
