import logging
import os
import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from models.cliente import Cliente
from models.habitacion import HabitacionDoble
from services.reserva_service import crear_reserva

# Configuración de logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Conexión base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "app.db")

def conectar_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

# Función para reservar desde la interfaz
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
        crear_reserva(cliente, habitacion, fecha_inicio_dt, fecha_fin_dt)
        messagebox.showinfo("Éxito", f"Reserva confirmada para {cliente.nombre}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Función para eliminar un cliente
def eliminar_cliente(nombre):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservas WHERE cliente_nombre = ?", (nombre,))
    conn.commit()
    conn.close()

# Función para crear las tablas
def crear_tablas():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_nombre TEXT NOT NULL,
            cliente_email TEXT NOT NULL,
            habitacion_numero INTEGER NOT NULL,
            precio REAL NOT NULL,
            fecha_inicio TEXT NOT NULL,
            fecha_fin TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Función principal (crea una reserva de prueba)
def main():
    cliente = Cliente("Francisco Perez", "franciscoperez@gmail.com")
    habitacion = HabitacionDoble(101, 100)
    fecha_inicio = datetime(2024, 10, 20)
    fecha_fin = datetime(2024, 10, 22)
    crear_reserva(cliente, habitacion, fecha_inicio, fecha_fin)

# Interfaz gráfica
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

# Programa principal
if __name__ == "__main__":
    crear_tablas()
    main()
    root.mainloop()
