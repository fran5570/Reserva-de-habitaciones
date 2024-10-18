class Factura:
    def __init__(self, numero, cliente, total):
        self.numero = numero
        self.cliente = cliente
        self.total = total
    
    def generar_factura(self):
        print(f"Generando factura para {self.cliente.nombre}. Total: {self.total}")