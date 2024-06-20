global ceros 
ceros = 7

class Codigo:
    def __init__(self):
        self.codigos = set({})

    def add_codigo(self, codigo):#para el excel
        self.codigos.add(codigo)

    def asignar_codigo(self):
        mx = 0
        for i in self.codigos:
            if int(i[3:]) > mx:
                mx = int(i[3:])
        mx += 1
        mx = str(mx)
        while len(mx) < ceros:
            mx = "0" + mx
        self.codigos.add("VIA" + mx)
        return "VIA" + mx






