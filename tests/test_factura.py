from models.cliente import Cliente
from models.factura import Factura

def test_generar_factura():
    cliente = Cliente("Francisco Pérez", "franciscoperez@gmail.com")
    factura = Factura(1, cliente, 500)
    factura.generar_factura()
    print("Test generar_factura completado con éxito.")
