import logging

logger = logging.getLogger(__name__)


class PagoService:
    def procesar_pago(self, monto):
        logger.info(f"Procesando pago de {monto} unidades monetarias...")
        return True