import Datos
import Asiento


class Bus:
    def __init__(self, tipo_bus, origen, destino, fecha, hora):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.tipo_bus = tipo_bus
        self.cantidad_asientos = Datos.cantidad_asientos_bus[tipo_bus]
        self.asientos = []
        self.inicializar_asientos()

    def mostrar_asientos_disponibles(self):
        lista = []
        for asiento in self.asientos:
            if not asiento.ocupado:
                lista.append(asiento.numero_asiento)
        return lista

    def cantidad_asientos_disponibles(self):
        cnt = 0
        for asiento in self.asientos:
            if not asiento.ocupado:
                cnt += 1
        return cnt
    
    def inicializar_asientos(self):
        for i in range(1, self.cantidad_asientos + 1):
            asiento = Asiento.Asiento(
                self.origen,
                self.destino,
                self.tipo_bus,
                i,
                self.fecha,
                self.hora
            )
            self.asientos.append(asiento)

    def mostrar_precios(self):
        for asiento in self.asientos:
            print(asiento.numero_asiento, asiento.precio)

    def get_Datos(self):
        return self.origen, self.destino, self.tipo_bus, self.fecha, self.hora


