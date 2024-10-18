import tkinter as tk
from tkinter import messagebox
from models.cliente import Cliente
from models.habitacion import HabitacionDoble
from services.reserva_service import crear_reserva
from datetime import datetime

def reservar():
    nombre = entry_nombre.get()
    email = entry_email.get()
    fecha_inicio = entry_fecha_inicio.get()
    fecha_fin = entry_fecha_fin.get()

    cliente = Cliente(nombre, email)
    habitacion = HabitacionDoble(101, 100)


    try:
        fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
        reserva = crear_reserva(cliente, habitacion, fecha_inicio_dt, fecha_fin_dt)
        messagebox.showinfo("Éxito", f"Reserva confirmada para {cliente.nombre}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Gestión de Reservas")


tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Fecha Inicio (YYYY-MM-DD):").pack()
entry_fecha_inicio = tk.Entry(root)
entry_fecha_inicio.pack()

tk.Label(root, text="Fecha Fin (YYYY-MM-DD):").pack()
entry_fecha_fin = tk.Entry(root)
entry_fecha_fin.pack()


tk.Button(root, text="Reservar", command=reservar).pack()


root.mainloop()
