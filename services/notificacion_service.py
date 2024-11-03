import logging

logger = logging.getLogger(__name__)


def enviar_confirmacion_email(cliente_email, reserva):
    logger.info(f"Enviando correo de confirmación a {cliente_email} para la reserva {reserva.habitacion.numero}.")
