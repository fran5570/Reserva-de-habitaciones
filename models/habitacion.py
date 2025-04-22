import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import sqlite3

class Habitacion:
    def __init__(self, numero: int, precio_base: float):
        self.numero = numero
        self.precio_base = precio_base
        self.ocupada = False

    def calcular_precio(self, noches):
        return self.precio_base * noches

    def marcar_ocupada(self):
        self.ocupada = True

    def marcar_disponible(self):
        self.ocupada = False

class HabitacionDoble(Habitacion):
    
    def calcular_precio(self, noches):
        self.numero
        self.precio_base
        return self.precio_base * noches * 1.2

class Suite(Habitacion):
    def calcular_precio(self, noches):
        return self.precio_base * noches * 1.5


class HabitacionFactory:
    _habitacion_map = {
        "simple": Habitacion,
        "doble": HabitacionDoble,
        "suite": Suite
    }

    @staticmethod
    def crear_habitacion(tipo, numero, precio_base):
        habitacion_cls = HabitacionFactory._habitacion_map.get(tipo)
        if habitacion_cls:
            logger.info(f"Creando habitación de tipo '{tipo}' con número {numero} y precio base {precio_base}.")
            return habitacion_cls(numero, precio_base)
        else:
            logger.error(f"Tipo de habitación desconocido: {tipo}")
            raise ValueError("Tipo de habitación desconocido.")