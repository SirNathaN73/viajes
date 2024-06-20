import Viaje
import Usuario
import Historial_Viajes
import Datos
import Bus
#libreria para leer excel
import pandas as pd


class Controlador:
    def __init__(self):
        self.historial = Historial_Viajes.Historial()

    def add_viaje_nuevo(self, origen, destino, tipo_bus, fecha, hora, asiento, comprobante):
        self.historial.add_viaje_nuevo(origen, destino, tipo_bus, fecha, hora, asiento, comprobante)

    def mostrar_tipos_buses(self):
        return Datos.tipo_bus
    
    def mostrar_destino_origen(self):
        return Datos.destino_origen
    
    def mostrar_precios(self, destino, tipo_bus):
        return Datos.precios[destino][tipo_bus]
    
    def get_precios(self):
        return Datos.precios

    def mostrar_horarios(self):
        return Datos.horarios
    
    def mostrar_asientos_disponibles(self, origen, destino, tipo_bus, fecha, hora):
        return self.historial.get_asientos_disponibles(origen, destino, tipo_bus, fecha, hora)
    
    def añadir_bus(self, origen, destino, tipo_bus, fecha, hora):
        return self.historial.add_bus(origen, destino, tipo_bus, fecha, hora)

    def generar_comprobante(self):
        return self.historial.generar_comprobante()
    
    def get_codigo(self, origen, destino, tipo_bus, fecha, hora):
        return self.historial.get_codigo(origen, destino, tipo_bus, fecha, hora)

    def init_buses(self, archivo):
        #leer excel
        try:
            df = pd.read_excel(archivo)
            for i in range(len(df)):
                origen = df["T_Origen"][i]
                destino = df["T_Destino"][i]
                tipo_bus = df["TipoBus"][i]
                fecha = df["Fecha"][i]
                fecha = str(fecha).split(" ")[0]
                fecha = fecha.split("-")
                d = int(fecha[2])
                m = fecha[1]
                a = fecha[0]
                fecha = str(d) + "/" + m + "/" + a
                hora = df["Horario"][i]
                codigo = df["CódigoViaje"][i]
                asiento = df["Asiento"][i]
                comprobante = df["CódigoComprobante"][i]
                self.historial.add_viaje_existente(origen, destino, tipo_bus, fecha, hora, codigo, asiento, comprobante)
        except:
            pass 

    def mostrar_buses(self):
        return self.historial.buses

