import logging
from services.notificacion_service import enviar_confirmacion_email
import sqlite3
from datetime import datetime
import os
from models.reserva import Reserva
from services.notificacion_service import enviar_confirmacion_email

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # sube un nivel desde services/
DB_PATH = os.path.join(BASE_DIR, "database", "app.db")

conn = sqlite3.connect(DB_PATH)


logger = logging.getLogger(__name__)


def crear_reserva(cliente, habitacion, fecha_inicio, fecha_fin):
    from datetime import datetime

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DB_PATH = os.path.join(BASE_DIR, "database", "app.db")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    noches = (fecha_fin - fecha_inicio).days
    cliente_nombre = cliente.nombre
    cliente_email = cliente.email
    habitacion_numero = habitacion.numero
    precio = habitacion.calcular_precio(noches)
    fecha_inicio_str = fecha_inicio.strftime('%Y-%m-%d')
    fecha_fin_str = fecha_fin.strftime('%Y-%m-%d')

    query = '''
        INSERT INTO reservas (cliente_nombre, cliente_email, habitacion_numero, precio, fecha_inicio, fecha_fin)
        VALUES (?, ?, ?, ?, ?, ?)
    '''
    
    cursor.execute(query, (cliente_nombre, cliente_email, habitacion_numero, precio, fecha_inicio_str, fecha_fin_str))

    conn.commit()
    conn.close()

def cancelar_reserva(reserva):
    reserva.habitacion.marcar_disponible()
    logger.info(f"Reserva de {reserva.cliente.nombre} ha sido cancelada.")