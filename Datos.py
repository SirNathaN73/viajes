
tipo_bus = ["VIP", "B1C", "BNE", "BEC"]

destino_origen = [
    "Lima",
    "Ica",
    "Arequipa",
    "Moquegua",
    "Tacna",
    "Chimbote",
    "Huaraz",
    "Trujillo",
    "Chiclayo",
    "Piura",
    "Tumbes"
]

cantidad_asientos_bus = {
    "VIP": 39,
    "B1C": 40,
    "BNE": 50,
    "BEC": 56
}

precios = {
    "Lima":{
        "Ica": {
            "VIP": {i: 200 if i <= 12 else 180 for i in range(1, 40)},#RANGO DE 1 A 39
            "B1C": {i: 192 if i <= 10 else 160 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 100 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 60 for i in range(1, 57)} #RANGO DE 1 A 56
        },
        "Arequipa": {
            "VIP": {i: 220 if i <= 12 else 200 for i in range(1, 40)},#RANGO DE 1 A 39
            "B1C": {i: 188 if i <= 10 else 156 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 120 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 80 for i in range(1, 57)}, #RANGO DE 1 A 56
        },
        "Moquegua": {
            "B1C": {i: 188 if i <= 10 else 156 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 128 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 80 for i in range(1, 57)}, #RANGO DE 1 A 56
        },
        "Tacna": {
            "VIP": {i: 240 if i <= 12 else 200 for i in range(1, 40)},#RANGO DE 1 A 39
            "B1C": {i: 200 if i <= 10 else 168 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 140 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 88 for i in range(1, 57)}, #RANGO DE 1 A 56
        },
        "Chimbote": {
            "B1C": {i: 184 if i <= 10 else 172 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 108 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 72 for i in range(1, 57)}, #RANGO DE 1 A 56
        },
        "Huaraz": {
            "VIP": {i: 212 if i <= 12 else 188 for i in range(1, 40)},#RANGO DE 1 A 39
            "B1C": {i: 184 if i <= 10 else 172 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 108 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 72 for i in range(1, 57)}, #RANGO DE 1 A 56
        },
        "Trujillo": {
            "VIP": {i: 212 if i <= 12 else 188 for i in range(1, 40)},#RANGO DE 1 A 39
            "B1C": {i: 184 if i <= 10 else 172 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 108 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 72 for i in range(1, 57)}, #RANGO DE 1 A 56
        },
        "Chiclayo": {
            "VIP": {i: 220 if i <= 12 else 200 for i in range(1, 40)},#RANGO DE 1 A 39
            "B1C": {i: 188 if i <= 10 else 156 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 120 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 80 for i in range(1, 57)}, #RANGO DE 1 A 56
        },
        "Piura": {
            "VIP": {i: 240 for i in range(1, 40)},#RANGO DE 1 A 39
            "B1C": {i: 220 if i <= 10 else 200 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 132 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 100 for i in range(1, 57)}, #RANGO DE 1 A 56
        },
        "Tumbes": {
            "VIP": {i: 248 for i in range(1, 40)},#RANGO DE 1 A 39
            "B1C": {i: 228 if i <= 10 else 200 for i in range(1, 41)},#RANGO DE 1 A 40
            "BNE": {i: 140 for i in range(1, 51)}, #RANGO DE 1 A 50
            "BEC": {i: 120 for i in range(1, 57)}, #RANGO DE 1 A 56
        }
    },
    #PRECIO DE REGRESO DE LIMA A OTRAS CIUDADES
    "Ica":{
        "VIP": {i: 200 if i <= 12 else 180 for i in range(1, 40)},#RANGO DE 1 A 39
        "B1C": {i: 192 if i <= 10 else 160 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 100 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 60 for i in range(1, 57)} #RANGO DE 1 A 56
    },
    "Arequipa":{
        "VIP": {i: 220 if i <= 12 else 200 for i in range(1, 40)},#RANGO DE 1 A 39
        "B1C": {i: 188 if i <= 10 else 156 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 120 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 80 for i in range(1, 57)}, #RANGO DE 1 A 56
    },
    "Moquegua":{
        "B1C": {i: 188 if i <= 10 else 156 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 128 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 80 for i in range(1, 57)}, #RANGO DE 1 A 56
    },
    "Tacna":{
        "VIP": {i: 240 if i <= 12 else 200 for i in range(1, 40)},#RANGO DE 1 A 39
        "B1C": {i: 200 if i <= 10 else 168 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 140 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 88 for i in range(1, 57)}, #RANGO DE 1 A 56
    },
    "Chimbote":{
        "B1C": {i: 184 if i <= 10 else 172 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 108 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 72 for i in range(1, 57)}, #RANGO DE 1 A 56
    },
    "Huaraz":{
        "VIP": {i: 212 if i <= 12 else 188 for i in range(1, 40)},#RANGO DE 1 A 39
        "B1C": {i: 184 if i <= 10 else 172 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 108 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 72 for i in range(1, 57)}, #RANGO DE 1 A 56
    },
    "Trujillo":{
        "VIP": {i: 212 if i <= 12 else 188 for i in range(1, 40)},#RANGO DE 1 A 39
        "B1C": {i: 184 if i <= 10 else 172 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 108 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 72 for i in range(1, 57)}, #RANGO DE 1 A 56
    },
    "Chiclayo":{
        "VIP": {i: 220 if i <= 12 else 200 for i in range(1, 40)},#RANGO DE 1 A 39
        "B1C": {i: 188 if i <= 10 else 156 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 120 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 80 for i in range(1, 57)}, #RANGO DE 1 A 56
    },
    "Piura":{
        "VIP": {i: 240 for i in range(1, 40)},#RANGO DE 1 A 39
        "B1C": {i: 220 if i <= 10 else 200 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 132 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 100 for i in range(1, 57)}, #RANGO DE 1 A 56
    },
    "Tumbes":{
        "VIP": {i: 248 for i in range(1, 40)},#RANGO DE 1 A 39
        "B1C": {i: 228 if i <= 10 else 200 for i in range(1, 41)},#RANGO DE 1 A 40
        "BNE": {i: 140 for i in range(1, 51)}, #RANGO DE 1 A 50
        "BEC": {i: 120 for i in range(1, 57)}, #RANGO DE 1 A 56
    }
}

horarios = {
    "Lima": {
        "Ica": ["6:00", "8:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"],
        "Arequipa": ["5:00", "7:00", "21:00", "23:00"],
        "Moquegua": ["5:00", "7:00", "21:00", "23:00"],
        "Tacna": ["5:00", "23:00"],
        "Chimbote": ["6:00", "7:00", "20:00", "21:00"],
        "Huaraz": ["5:00", "7:00", "21:00", "23:00"],
        "Trujillo": ["6:00", "7:00", "22:00", "23:00"],
        "Chiclayo": ["6:00", "7:00", "22:00", "23:00"],
        "Piura": ["5:00", "23:00"],
        "Tumbes": ["5:00", "23:00"]
    },
    "Ica": {
        "Lima": ["6:00", "8:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]
    },
    "Arequipa": {
        "Lima": ["5:00", "7:00", "21:00", "23:00"]
    },
    "Moquegua": {
        "Lima": ["5:00", "7:00", "21:00", "23:00"]
    },
    "Tacna": {
        "Lima": ["5:00", "23:00"]
    },
    "Chimbote": {
        "Lima": ["6:00", "7:00", "20:00", "21:00"]
    },
    "Huaraz": {
        "Lima": ["5:00", "7:00", "21:00", "23:00"]
    },
    "Trujillo": {
        "Lima": ["6:00", "7:00", "22:00", "23:00"]
    },
    "Chiclayo": {
        "Lima": ["6:00", "7:00", "22:00", "23:00"]
    },
    "Piura": {
        "Lima": ["5:00", "23:00"]
    },
    "Tumbes": {
        "Lima": ["5:00", "23:00"]
    }
}

