import Controlador
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

class Terminal:
    def __init__(self, root):
        self.controlador = Controlador.Controlador()
        self.root = root
        self.root.title("ConexiónViajera")
        self.controlador.init_buses("databus.xlsx")
        self.df = pd.read_excel("databus.xlsx")
        self.entry_values ={}

    def show_inicio_screen(self):
        self.inicio_screen = ttk.Frame(self.root, width=1200, height=1000)
        self.inicio_screen.pack()        
        ttk.Label(self.inicio_screen, text="Bienvenido a ConexiónViajera", font=("Flexo", 20, "bold")).pack(pady=50, padx=100)
        ttk.Button(self.inicio_screen, text="Iniciar Búsqueda", command=self.show_search_screen).pack(pady=20)
        ttk.Button(self.inicio_screen, text="Generar Histograma", command=self.show_histogram).pack(pady=30)
    
    def show_histogram(self):
        self.inicio_screen.destroy()
        self.histogram_frame = ttk.Frame(self.root, width=1200, height=1000)
        self.histogram_frame.pack()
        ttk.Label(self.histogram_frame, text="Histograma de Viajes", font=("Flexo", 20, "bold")).pack(pady=50, padx=100)
        ttk.Label(self.histogram_frame, text="Seleccione el tipo de bus:").pack()
        tbus_var = tk.StringVar()
        tbus_entry = ttk.Combobox(self.histogram_frame, textvariable=tbus_var, state="readonly")
        tbus_entry['values'] = self.controlador.mostrar_tipos_buses()
        tbus_entry.current(0)
        tbus_entry.pack(pady=5)
        ttk.Button(self.histogram_frame, text="Generar Histograma", command=lambda: self.show_graph(tbus_entry.get())).pack(pady=10)
        #ttk.Button(self.histogram_frame, text="Volver", command=self.volver4).pack(pady=10)

    def show_graph(self, tbus):
        df = self.df
        df = df[df["TipoBus"] == tbus]
        df = df["T_Destino"].value_counts()
        df = df.sort_index()
        df.plot(kind="bar")
        plt.show()


    def show_search_screen(self):
        self.inicio_screen.destroy()
        self.search_screen = ttk.Frame(self.root, width=1200, height=1000)
        self.search_screen.pack()        
        ttk.Label(self.search_screen, text="Buscar Viaje", font=("Flexo", 20, "bold")).pack(pady=50, padx=100)             

        #Terminal de origen
        ttk.Label(self.search_screen,text="Terminal de origen:").pack()
        origen_var = tk.StringVar()
        origen_entry=ttk.Combobox(self.search_screen, textvariable=origen_var, state="readonly")
        origen_entry['values'] = self.controlador.mostrar_destino_origen()
        origen_entry.current(0)
        origen_entry.pack(pady=5)
        self.entry_values["Origen"]=origen_entry
        
        #Terminal de destino
        ttk.Label(self.search_screen,text="Terminal de destino:").pack()
        destino_var = tk.StringVar()
        destino_entry=ttk.Combobox(self.search_screen, textvariable=destino_var, state="readonly")
        destino_entry['values'] = self.controlador.mostrar_destino_origen()
        destino_entry.current(0)
        destino_entry.pack(pady=5)
        self.entry_values["Destino"]=destino_entry
        
        #Fecha de viaje
        ttk.Label(self.search_screen,text="Fecha de viaje:").pack()
        fecha_entry = DateEntry(self.search_screen, width=12, locale='es_PE', date_pattern="d/mm/y")
        fecha_entry.pack(pady=5)
        self.entry_values["Fecha"]=fecha_entry
        #fecha_entry.bind("<<DateEntrySelected>>", self.obtener_fecha)
        self.entry_values["Fecha"].bind("<<DateEntrySelected>>")
        
        
        #Tipo de bus
        ttk.Label(self.search_screen,text="Tipo de bus:").pack()
        tbus_var = tk.StringVar()
        tbus_entry = ttk.Combobox(self.search_screen, textvariable=tbus_var, state="readonly")
        #VIP, B1C , BNE, BEC
        tbus_entry['values'] = self.controlador.mostrar_tipos_buses()
        tbus_entry.current(0)
        tbus_entry.pack(pady=5)
        self.entry_values["Tbus"]=tbus_entry

        #Horario de viaje
        ttk.Label(self.search_screen, text="Horario de Viaje:").pack()
        self.horario_var = tk.StringVar()
        self.horario_combobox = ttk.Combobox(self.search_screen, textvariable=self.horario_var, state="readonly")
        self.horario_combobox.pack(pady=5)
        

        self.entry_values["Origen"].bind("<<ComboboxSelected>>", self.actualizar_horarios)
        self.entry_values["Destino"].bind("<<ComboboxSelected>>", self.actualizar_horarios)
        ttk.Button(self.search_screen, text="Buscar", command=self.search_trip).pack(pady=10)  
               
    def actualizar_horarios(self, event):
        origen = self.entry_values["Origen"].get()
        destino = self.entry_values["Destino"].get()
        horarios = self.controlador.mostrar_horarios()


        if destino in horarios[origen]:
            selec = horarios[origen][destino]
            self.horario_combobox['values'] = selec
            self.horario_combobox.current(0)
        else:
            self.horario_combobox['values'] = []
            self.horario_combobox.set("")

    def search_trip(self):
        origen = self.entry_values["Origen"].get()
        destino = self.entry_values["Destino"].get()
        fecha = self.entry_values["Fecha"].get()
        tbus = self.entry_values["Tbus"].get()
        horario = self.horario_combobox.get()

        

        if origen == "" or destino == "" or fecha == "" or tbus == "" or horario == "":
            messagebox.showerror("Error", "Por favor, llene todos los campos")
            return
        
        dest = origen
        if origen == 'Lima':
            dest = destino
        if tbus not in self.controlador.get_precios()[dest]:
            messagebox.showerror("Error", "No disponemos de buses " + tbus + " para el viaje seleccionado")
            return
        
        self.controlador.añadir_bus(origen, destino, tbus, fecha, horario)
        asientos = self.controlador.mostrar_asientos_disponibles(origen, destino, tbus, fecha, horario)
        self.show_seat_selection(asientos, origen, destino, tbus, fecha, horario)


    def show_seat_selection(self, asientos, origen, destino, tbus, fecha, horario):
        self.aux_origen = origen
        self.aux_destino = destino
        self.aux_tbus = tbus
        self.aux_fecha = fecha
        self.aux_horario = horario
        self.search_screen.destroy()
        self.seat_selection_frame = ttk.Frame(self.root)
        self.seat_selection_frame.pack_propagate(0)
        self.seat_selection_frame.config(width=300, height=300)
        self.seat_selection_frame.pack(fill="both", expand=True)
    
        

        ttk.Label(self.seat_selection_frame, text="INFORMACIÓN", font=("Flexo", 10, "bold")).pack()

        self.frame_seats = ttk.Frame(self.seat_selection_frame)
        self.frame_seats.pack()
        ttk.Label(self.frame_seats, text="Origen:           "+origen, font=(None, 10, "italic")).pack(anchor="w")
        ttk.Label(self.frame_seats, text="Destino:          "+destino, font=(None, 10, "italic")).pack(anchor="w")
        ttk.Label(self.frame_seats, text="Fecha:            "+fecha, font=(None, 10, "italic")).pack(anchor="w")
        ttk.Label(self.frame_seats, text="Tipo de bus:   "+tbus, font=(None, 10, "italic")).pack(anchor="w")
        ttk.Label(self.frame_seats, text="Horario:          "+horario, font=(None, 10, "italic")).pack(anchor="w")


        ttk.Label(self.seat_selection_frame, text="Seleccionar asiento:", font=("Flexo", 10)).pack(padx=10, pady=10)
        self.seat_var = tk.StringVar()
        self.seat_combobox = ttk.Combobox(self.seat_selection_frame, textvariable=self.seat_var, state="readonly")
        self.seat_combobox['values'] = asientos
        self.seat_combobox.pack(pady=5)

        self.price_var = tk.StringVar()
        ttk.Label(self.seat_selection_frame, text="Precio:").pack()
        self.price_entry = ttk.Entry(self.seat_selection_frame, textvariable=self.price_var, state="readonly")
        self.price_entry.pack(pady=5)

        
       
        self.seat_combobox.bind("<<ComboboxSelected>>", self.actualizar_precio)

        self.frame_botones = ttk.Frame(self.seat_selection_frame)
        self.frame_botones.pack()

        ttk.Button(self.frame_botones, text="Reservar", command=self.reservar_viaje).pack(pady=10, side="left")
        ttk.Button(self.frame_botones, text="Cancelar", command=self.volver1).pack(pady=10, side="left")
    
    def actualizar_precio(self, event):
        origen = self.aux_origen
        destino = self.aux_destino
        tbus = self.aux_tbus
        asiento = int(self.seat_combobox.get())

        
        dest = origen
        if origen == 'Lima':
            dest = destino

        precio = self.controlador.get_precios()[dest][tbus][asiento]
        self.price_var.set(precio)

    def volver1(self):
        self.seat_selection_frame.destroy()
        self.show_search_screen()
    
    def volver2(self):
        self.register_frame.destroy()
        self.show_search_screen()

    def volver3(self):
        self.compra_frame.destroy()
        self.show_search_screen()

    def reservar_viaje(self):
        
        self.aux_asiento = self.seat_combobox.get()
        self.aux_precio = self.price_var.get()

        self.seat_selection_frame.destroy()
        self.register_frame = ttk.Frame(self.root)
        self.register_frame.pack_propagate(0)
        self.register_frame.config(width=450, height=380)
        self.register_frame.pack(fill="both", expand=True)

        ttk.Label(self.register_frame, text="Registrar Datos", font=("Flexo", 20, "bold")).pack(pady=10)

        ttk.Label(self.register_frame, text="DNI:").pack()
        self.entry_dni = ttk.Entry(self.register_frame, width=30)
        self.entry_dni.pack(pady=5)

        ttk.Label(self.register_frame, text="Nombres:").pack()
        self.entry_name = ttk.Entry(self.register_frame, width=30)
        self.entry_name.pack(pady=5)

        ttk.Label(self.register_frame, text="Apellidos:").pack()
        self.entry_last_name = ttk.Entry(self.register_frame, width=30)
        self.entry_last_name.pack(pady=5)

        ttk.Label(self.register_frame, text="Correo:").pack()
        self.entry_email = ttk.Entry(self.register_frame, width=30)
        self.entry_email.pack(pady=5)

        ttk.Label(self.register_frame, text="Teléfono:").pack()
        self.entry_phone = ttk.Entry(self.register_frame, width=30)
        self.entry_phone.pack(pady=5)

        self.frame_botones = ttk.Frame(self.register_frame)
        self.frame_botones.pack()

        ttk.Button(self.frame_botones, text="Registrar datos", command=self.mostrar_compra).pack(pady=10, side="left")
        ttk.Button(self.frame_botones, text="Cancelar", command=self.volver2).pack(pady=10, side="left")
        
    def mostrar_compra(self):
        self.aux_dni = self.entry_dni.get()
        self.aux_name = self.entry_name.get()
        self.aux_last_name = self.entry_last_name.get()
        self.aux_email = self.entry_email.get()
        self.aux_phone = self.entry_phone.get()

        if self.aux_dni == "" or self.aux_name == "" or self.aux_last_name == "" or self.aux_email == "" or self.aux_phone == "":
            messagebox.showerror("Error", "Por favor, llene todos los campos")
            return
        
        self.register_frame.destroy()

        self.compra_frame = ttk.Frame(self.root)
        self.compra_frame.pack_propagate(0)
        self.compra_frame.config(width=350, height=270)
        self.compra_frame.pack(fill="both", expand=True)

        ttk.Label(self.compra_frame, text="Comprar Boleto", font=("Flexo", 20, "bold")).pack(pady=10)

        comprobante = self.controlador.generar_comprobante()
        codigo = self.controlador.get_codigo(self.aux_origen, self.aux_destino, self.aux_tbus,
                                             self.aux_fecha, self.aux_horario)
        
        ttk.Label(self.compra_frame, text="Código de Comprobante:").pack()
        self.entry_comprobante = ttk.Entry(self.compra_frame)
        self.entry_comprobante.insert(0, comprobante)
        self.entry_comprobante.config(state=tk.DISABLED, foreground= "gray")
        self.entry_comprobante.pack(pady=5)
        
        ttk.Label(self.compra_frame, text="Código de Viaje:").pack()
        self.entry_codigo = ttk.Entry(self.compra_frame)
        self.entry_codigo.insert(0, codigo)
        self.entry_codigo.config(state=tk.DISABLED, foreground= "gray")
        self.entry_codigo.pack(pady=5)

        ttk.Label(self.compra_frame, text="Medio de Pago:").pack()
        self.payment_var = tk.StringVar()
        self.payment_combobox = ttk.Combobox(self.compra_frame, textvariable=self.payment_var, state="readonly")
        self.payment_combobox['values'] = ["Efectivo", "Tarjeta", "Plin", "Yape"]
        self.payment_combobox.pack(pady=5)

        self.frame_botones = ttk.Frame(self.compra_frame)
        self.frame_botones.pack()

        ttk.Button(self.frame_botones, text="Finalizar Compra", command=self.finalizar_compra).pack(pady=10, side = "left")
        ttk.Button(self.frame_botones, text="Cancelar", command=self.volver3).pack(pady=10, side = "left")

    def finalizar_compra(self):
        
        pago = self.payment_combobox.get()
        if pago == "":
            messagebox.showerror("Error", "Por favor, seleccione un medio de pago")
            return
        
        self.aux_codigo_viaje = self.entry_codigo.get()
        self.aux_comprobante = self.entry_comprobante.get()
        self.aux_meto_pago = pago

        self.controlador.add_viaje_nuevo(self.aux_origen, self.aux_destino, self.aux_tbus,
                                         self.aux_fecha, self.aux_horario, int(self.aux_asiento),
                                         self.aux_comprobante)


        #self.aux_fecha a formato yyyy-mm-dd segundos-minutos-horas

  
        self.aux_fecha = self.aux_fecha.split("/")
        d = int(self.aux_fecha[0])
        m = int(self.aux_fecha[1])
        a = int(self.aux_fecha[2])
        self.aux_fecha = date(a, m, d)
        df_aux = pd.DataFrame({"CódigoComprobante": [self.aux_comprobante],
                               "CódigoViaje": [self.aux_codigo_viaje],
                               "T_Origen": [self.aux_origen],
                               "T_Destino": [self.aux_destino],
                               "Fecha": [self.aux_fecha],
                               "TipoBus": [self.aux_tbus],
                               "Horario": [self.aux_horario],
                               "Asiento": [int(self.aux_asiento)],
                               "Precio": [int(self.aux_precio)],
                               "DNI": [self.aux_dni],
                               "Nombres": [self.aux_name],
                               "Apellidos": [self.aux_last_name],
                               "Correo": [self.aux_email],
                               "Teléfono": [int(self.aux_phone)],
                               "TipoPago": [self.aux_meto_pago]})
        

        self.df = pd.concat([self.df, df_aux], ignore_index=True)
        
        self.df.to_excel("databus.xlsx", index=False)

        messagebox.showinfo("Compra Exitosa", "Compra realizada con éxito")

        self.compra_frame.destroy()
        self.show_inicio_screen()
        

        
        
    
        
        
        


if __name__ == "__main__":

    root = tk.Tk()
    app = Terminal(root)
    app.show_inicio_screen()
    root.mainloop()
