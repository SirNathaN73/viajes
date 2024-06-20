import Bus

class Viaje:
    def __init__(self, origen, destino, tipo_bus, fecha, hora):
        self.bus = Bus.Bus(tipo_bus, origen, destino, fecha, hora)
        self.codigo = None
        self.usuarios = []


    def add_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.bus.asientos[usuario.numero_asiento - 1].ocupar_asiento()

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            usuario.mostrar_datos()

    def mostrar_asientos_disponibles(self):
        self.bus.mostrar_asientos_disponibles()

    def get_Codigo(self):
        return self.codigo
    
    def get_Datos(self):
        return self.bus.origen, self.bus.destino, self.bus.tipo_bus, self.bus.fecha, self.bus.hora
    