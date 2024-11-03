import logging
from models.reserva import Reserva
from services.notificacion_service import enviar_confirmacion_email

logger = logging.getLogger(__name__)


def crear_reserva(cliente, habitacion, fecha_inicio, fecha_fin):
    reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
    reserva.confirmar_reserva()
    enviar_confirmacion_email(cliente.email, reserva)
    return reserva

def cancelar_reserva(reserva):
    reserva.habitacion.marcar_disponible()
    logger.info(f"Reserva de {reserva.cliente.nombre} ha sido cancelada.")
