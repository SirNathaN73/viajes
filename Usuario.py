class Usuario:
    def __init__(self, nombre, apellido, dni, correo, telefono, numero_asiento):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo = correo
        self.telefono = telefono
        self.numero_asiento = int(numero_asiento)
        self.pago = None

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Correo: {self.correo}")
        print(f"Telefono: {self.telefono}")

   