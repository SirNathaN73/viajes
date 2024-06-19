import random

global ceros 
ceros = 10

class Comprobante:
    def __init__(self):
        self.comprobantes = set({})

    def add_comprobante(self, codigo):#para el excel
        self.comprobantes.add(codigo)

    def generar_comprobante(self):
        mx = 0
        while True:
            mx = random.randint(0, 9999999999)
            if str(mx) not in self.comprobantes:
                break
        
        mx = str(mx)
        while len(mx) < ceros:
            mx = "0" + mx
        return "NOT" + mx








