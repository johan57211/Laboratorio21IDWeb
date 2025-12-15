import math

class Figura:
    def area(self):
        raise NotImplementedError("Debe implementar area()")

    def perimetro(self):
        raise NotImplementedError("Debe implementar perimetro()")

    def __str__(self):
        return f"{self.__class__.__name__} - Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}"
