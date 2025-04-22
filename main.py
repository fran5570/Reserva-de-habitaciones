import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

from models.cliente import Cliente
from models.habitacion import HabitacionDoble
from services.reserva_service import crear_reserva
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "app.db")

conn = sqlite3.connect(DB_PATH)



def conectar_db():
    conn = sqlite3.connect(DB_PATH)
    return conn


def main():

    cliente = Cliente("Francisco perez", "franciscoperez@gmail.com")

    
    habitacion = HabitacionDoble(101, 100)

    
    from datetime import datetime
    fecha_inicio = datetime(2024, 10, 20)
    fecha_fin = datetime(2024, 10, 22)

    
    crear_reserva(cliente, habitacion, fecha_inicio, fecha_fin)



def crear_tablas():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "database", "app.db")

    # Crea la carpeta 'database' si no existe
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
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


if __name__ == "__main__":
    crear_tablas()
    main()
