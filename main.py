import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

from models.cliente import Cliente
from models.habitacion import HabitacionDoble
from services.reserva_service import crear_reserva

def main():

    cliente = Cliente("Francisco perez", "franciscoperez@gmail.com")

    
    habitacion = HabitacionDoble(101, 100)

    
    from datetime import datetime
    fecha_inicio = datetime(2024, 10, 20)
    fecha_fin = datetime(2024, 10, 22)

    
    crear_reserva(cliente, habitacion, fecha_inicio, fecha_fin)

if __name__ == "__main__":
    main()
