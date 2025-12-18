import math

class Figura:
    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
