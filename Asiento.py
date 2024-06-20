import Datos

class Asiento:
    def __init__(self, origen, destino, tipo_bus, numero_asiento, fecha, hora):
        self.numero_asiento = numero_asiento
        self.ocupado = False
        self.destino = destino
        self.origen = origen
        self.tipo_bus = tipo_bus
        self.precio = 0
        self.fecha = fecha
        self.hora = hora
        self.poner_precio()

    def ocupar_asiento(self):
        self.ocupado = True

    def desocupar_asiento(self):
        self.ocupado = False

    def poner_precio(self):
        if self.destino == "Lima":
            self.origen, self.destino = self.destino, self.origen

        self.precio = Datos.precios[self.destino][self.tipo_bus][self.numero_asiento]



