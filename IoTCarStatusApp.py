import tkinter as tk
from tkinter import messagebox
from ApiUtils import inyectar_accion, obtener_hora_local, obtener_ip_cliente, obtener_historial


class IoTCarStatusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Car Status App")

        # Crear botones de control
        self.crear_botones()

        # Crear etiquetas para la hora y la IP
        self.hora_label = tk.Label(self.root, text="Hora: No disponible")
        self.hora_label.pack()

        self.ip_label = tk.Label(self.root, text="IP: No disponible")
        self.ip_label.pack()

        # Crear área de texto para el historial
        self.historial_area = tk.Text(self.root, height=10, width=50)
        self.historial_area.pack()

        # Botón para mostrar el historial
        self.historial_button = tk.Button(self.root, text="Historial", command=self.mostrar_historial)
        self.historial_button.pack()

        # Actualizar la hora y la IP al iniciar
        self.actualizar_hora_ip()

    def crear_botones(self):
        # Crear un frame para los botones
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        # Botones de dirección
        self.arriba_button = tk.Button(control_frame, text="Arriba", command=lambda: self.accion("Arriba"))
        self.arriba_button.grid(row=0, column=1)

        self.abajo_button = tk.Button(control_frame, text="Abajo", command=lambda: self.accion("Abajo"))
        self.abajo_button.grid(row=2, column=1)

        self.izquierda_button = tk.Button(control_frame, text="Izquierda", command=lambda: self.accion("Izquierda"))
        self.izquierda_button.grid(row=1, column=0)

        self.derecha_button = tk.Button(control_frame, text="Derecha", command=lambda: self.accion("Derecha"))
        self.derecha_button.grid(row=1, column=2)

    # Método para inyectar la acción en MockAPI
    def accion(self, accion):
        resultado = inyectar_accion(accion)
        messagebox.showinfo("Resultado", resultado)

    # Método para mostrar el historial
    def mostrar_historial(self):
        historial = obtener_historial()
        if isinstance(historial, list):
            self.historial_area.delete('1.0', tk.END)
            for registro in historial:
                self.historial_area.insert(tk.END,
                                           f"ID: {registro['id']}, Acción: {registro['accion']}, Fecha: {registro['date']}\n")
        else:
            messagebox.showerror("Error", historial)

    # Método para actualizar la hora y la IP
    def actualizar_hora_ip(self):
        hora = obtener_hora_local()
        if 'Error' in hora:
            hora = 'Hora no disponible'
        self.hora_label.config(text=f"Hora: {hora}")

        ip = obtener_ip_cliente()
        if 'Error' in ip:
            ip = 'IP no disponible'
        self.ip_label.config(text=f"IP: {ip}")


if __name__ == "__main__":
    root = tk.Tk()
    app = IoTCarStatusApp(root)
    root.mainloop()
