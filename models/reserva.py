from datetime import datetime
from models.habitacion import Habitacion

class Reserva:
    def __init__(self, cliente, habitacion: Habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_reserva = datetime.now()

    def calcular_total(self):
        noches = (self.fecha_fin - self.fecha_inicio).days
        return self.habitacion.calcular_precio(noches)

    def confirmar_reserva(self):
        self.habitacion.marcar_ocupada()
        print(f"Reserva confirmada para {self.cliente.nombre}. Total a pagar: {self.calcular_total()}")
