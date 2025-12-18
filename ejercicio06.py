import json

# Lista de equipos de fútbol
equipos = [
    {
        "nombre": "Real Madrid",
        "pais": "España",
        "nivelAtaque": 90,
        "nivelDefensa": 85
    },
    {
        "nombre": "Manchester City",
        "pais": "Inglaterra",
        "nivelAtaque": 88,
        "nivelDefensa": 87
    },
    {
        "nombre": "Bayern Munich",
        "pais": "Alemania",
        "nivelAtaque": 92,
        "nivelDefensa": 84
    }
]

json_equipos = json.dumps(equipos, indent=4, ensure_ascii=False)

print(json_equipos)
