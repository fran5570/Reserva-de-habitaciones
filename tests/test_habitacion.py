from models.habitacion import Habitacion, HabitacionDoble, Suite

def test_calcular_precio():
    habitacion = Habitacion(101, 100)
    assert habitacion.calcular_precio(2) == 200, "El precio debería ser 20000"

    habitacion_doble = HabitacionDoble(102, 100)
    assert habitacion_doble.calcular_precio(2) == 240, "El precio debería ser 80000"

    suite = Suite(103, 100)
    assert suite.calcular_precio(2) == 300, "El precio debería ser 100000"

    print("Test calcular_precio completado con éxito.")
