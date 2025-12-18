from geometria import Rectangulo, Triangulo, Circulo

figuras = [
    Rectangulo(5, 3),
    Triangulo(4, 3, 5, 5),
    Circulo(2)
]

for figura in figuras:
    print("Figura:", figura.__class__.__name__)
    print("Área:", figura.area())
    print("Perímetro:", figura.perimetro())
    print("-" * 30)
