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
        return self.precio_base * noches * 1.2

class Suite(Habitacion):
    def calcular_precio(self, noches):
        return self.precio_base * noches * 1.5


class HabitacionFactory:
    @staticmethod
    def crear_habitacion(tipo, numero, precio_base):
        if tipo == "simple":
            return Habitacion(numero, precio_base)
        elif tipo == "doble":
            return HabitacionDoble(numero, precio_base)
        elif tipo == "suite":
            return Suite(numero, precio_base)
        else:
            raise ValueError("Tipo de habitación desconocido.")