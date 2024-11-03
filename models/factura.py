import logging
logger = logging.getLogger(__name__)

class Factura:
    def __init__(self, numero, cliente, total):
        self.numero = numero
        self.cliente = cliente
        self.total = total
    
    def generar_factura(self):
        logger.info(f"Generando factura para {self.cliente.nombre}. Total: {self.total}")