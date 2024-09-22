import tkinter as tk
from tkinter import messagebox
from ApiUtils import obtener_hora_local, obtener_ip_cliente, inyectar_accion, obtener_historial


class IoTCarStatusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IoT Car Status")

        # Crear botones de acciones
        self.create_buttons()

        # Crear área de historial
        self.historial_area = tk.Text(root, height=10, width=50)
        self.historial_area.pack()

        # Crear área de información de hora e IP
        self.info_frame = tk.Frame(root)
        self.info_frame.pack()

        self.hora_label = tk.Label(self.info_frame, text="Hora: ")
        self.hora_label.grid(row=0, column=0)

        self.ip_label = tk.Label(self.info_frame, text="IP: ")
        self.ip_label.grid(row=1, column=0)

        # Actualizar la hora e IP
        self.actualizar_hora_ip()

    def create_buttons(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        self.btn_arriba = tk.Button(control_frame, text="Arriba", command=lambda: self.accion("Arriba"))
        self.btn_arriba.grid(row=0, column=1)

        self.btn_abajo = tk.Button(control_frame, text="Abajo", command=lambda: self.accion("Abajo"))
        self.btn_abajo.grid(row=2, column=1)

        self.btn_izquierda = tk.Button(control_frame, text="Izquierda", command=lambda: self.accion("Izquierda"))
        self.btn_izquierda.grid(row=1, column=0)

        self.btn_derecha = tk.Button(control_frame, text="Derecha", command=lambda: self.accion("Derecha"))
        self.btn_derecha.grid(row=1, column=2)

        self.btn_historial = tk.Button(control_frame, text="Historial", command=self.mostrar_historial)
        self.btn_historial.grid(row=3, column=1)

    def accion(self, direccion):
        resultado = inyectar_accion(direccion)
        messagebox.showinfo("Resultado", resultado)

    def mostrar_historial(self):
        historial = obtener_historial()
        if isinstance(historial, list):
            self.historial_area.delete('1.0', tk.END)
            for registro in historial:
                self.historial_area.insert(tk.END,
                                           f"ID: {registro['id']}, Acción: {registro['accion']}, Creado: {registro['createdAt']}\n")
        else:
            messagebox.showerror("Error", historial)

    def actualizar_hora_ip(self):
        self.hora_label.config(text=f"Hora: {obtener_hora_local()}")
        self.ip_label.config(text=f"IP: {obtener_ip_cliente()}")
