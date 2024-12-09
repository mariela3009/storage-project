import tkinter as tk
from tkinter import messagebox

#Mariela Ramos
def show_reservacion():
    global entradas
    reservacion = tk.Tk()
    reservacion.title("Agendar Cita")

    wventana = 854
    hventana = 480
    pwidth = round(reservacion.winfo_screenwidth() / 2 - wventana / 2)
    pheight = round(reservacion.winfo_screenheight() / 2 - hventana / 2)
    reservacion.geometry(f"{wventana}x{hventana}+{pwidth}+{pheight}")

    # Marco para la lista de servicios
    menu_frame = tk.Frame(reservacion)
    menu_frame.place(relx=1/6, rely=0.5, relwidth=1/3, anchor="center")

    lista_servicios = ["Esmaltado", "Semipermanente", "Gel", "Esculpidas"]
    for servicio in lista_servicios:
        label = tk.Button(menu_frame, text=servicio)
        label.pack(pady=5)
    

    # Marco para los campos de entrada
    campo_frame = tk.Frame(reservacion)
    campo_frame.place(relx=2/3, rely=0.5, relwidth=1/2, anchor="center")

    entradas = []
    campos = ["Nombre", "Teléfono", "Fecha", "Hora"]
    for campo in campos:
        etiqueta = tk.Label(campo_frame, text=campo)
        etiqueta.pack(fill=tk.X, pady=5)
        entrada = tk.Entry(campo_frame, width=40)
        entrada.pack(fill=tk.X, pady=5)
        entradas.append(entrada)

    boton_agendar = tk.Button(campo_frame, text="Agendar", command=verificar_casillas)
    boton_agendar.pack(pady=20)

    reservacion.mainloop()

def verificar_casillas():
    for entry in entradas:
        if not entry.get().strip():
            messagebox.showwarning("Advertencia", "Debe completar todas las casillas para continuar.")
            return
    