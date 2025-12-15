from Figura import Figura
import math

class Triangulo(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (math.sqrt(3) / 4) * self.lado ** 2

    def perimetro(self):
        return 3 * self.lado
