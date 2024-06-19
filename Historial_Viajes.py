import Codigo
import Comprobante
import Bus

class Historial:
    def __init__(self):
        self.historial_viajes = dict({})#para saber si ya existe un viaje
        self.codigo = Codigo.Codigo()
        self.comprobante = Comprobante.Comprobante()
        self.buses = []
        #ejemplo de uso: self.asiento_por_viaje["LimaArequipaVIP2021-10-1010:00"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def add_bus(self, origen, destino, tipo_bus, fecha, hora):
        bus = Bus.Bus(tipo_bus, origen, destino, fecha, hora)
        if self.buscar_bus(bus) == None:
            self.buses.append(bus)
        return bus
    

    def add_viaje_nuevo(self, origen, destino, tipo_bus, fecha, hora, asiento, comprobante):
        #Añade el comprobante
        self.comprobante.add_comprobante(comprobante)
        #Añade el viaje al historial
        new_viaje = str(origen) + str(destino) + str(tipo_bus) + str(fecha) + str(hora)
        if new_viaje not in self.historial_viajes:
            self.historial_viajes[new_viaje]= self.codigo.asignar_codigo()
        #Añade el bus si no existe
        bus = Bus.Bus(tipo_bus, origen, destino, fecha, hora)
        if self.buscar_bus(bus) == None:
            self.buses.append(bus)
        #Añade los asientos ocupados
        bus = self.buscar_bus(bus)
        bus.asientos[asiento - 1].ocupar_asiento()
        
    def generar_comprobante(self):
        comp = self.comprobante.generar_comprobante()
        return comp
    
    def add_viaje_existente(self, origen, destino, tipo_bus, fecha, hora, codigo, asiento, comprobante):
        #Añade el comprobante
        self.comprobante.add_comprobante(comprobante)
        #Añade el viaje al historial y al codigo
        viaje = str(origen) + str(destino) + str(tipo_bus) + str(fecha) + str(hora)
        self.codigo.add_codigo(codigo)
        self.historial_viajes[viaje] = codigo
        #Añade el bus
        bus = Bus.Bus(tipo_bus, origen, destino, fecha, hora)
        if self.buscar_bus(bus) == None:
            self.buses.append(bus)
        #Añade los asientos ocupados
        bus = self.buscar_bus(bus)#chancamos el bus con el que ya esta en la lista
        bus.asientos[asiento - 1].ocupar_asiento()

    def get_asientos_disponibles(self, origen, destino, tipo_bus, fecha, hora):
        bus = Bus.Bus(tipo_bus, origen, destino, fecha, hora)
        bus = self.buscar_bus(bus)
        return bus.mostrar_asientos_disponibles()
        
    

    def get_codigo(self, origen, destino, tipo_bus, fecha, hora):
        viaje = str(origen) + str(destino) + str(tipo_bus) + str(fecha) + str(hora)
        if viaje in self.historial_viajes:
            return self.historial_viajes[viaje]
        else:
            new_codigo = self.codigo.asignar_codigo()
            self.historial_viajes[viaje] = new_codigo
            return new_codigo

    def buscar_bus(self, bus_a_buscar):
        for bus in self.buses:
            if bus.get_Datos() == bus_a_buscar.get_Datos():
                return bus
        return None

