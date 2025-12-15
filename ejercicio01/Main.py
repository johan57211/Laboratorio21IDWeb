from Rectangulo import Rectangulo
from Triangulo import Triangulo
from Circulo import Circulo

figuras = [
    Rectangulo(4, 6),
    Triangulo(5),
    Circulo(3)
]

for figura in figuras:
    print(figura)
