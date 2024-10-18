from models.cliente import Cliente
from models.habitacion import HabitacionDoble
from models.reserva import Reserva
from datetime import datetime

def test_calcular_total():
    cliente = Cliente("Juan Pérez", "juan@example.com")
    habitacion = HabitacionDoble(101, 100)
    fecha_inicio = datetime(2024, 10, 20)
    fecha_fin = datetime(2024, 10, 22)
    reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
    
    assert reserva.calcular_total() == 240, "El total debería ser 240"
    print("Test calcular_total completado con éxito.")