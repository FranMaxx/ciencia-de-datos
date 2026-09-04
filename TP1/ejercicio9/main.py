class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def calcularArea(self):
        return self.alto * self.ancho

    def calcularPerimetro(self):
        return 2 * (self.alto + self.ancho)

rectangulo = Rectangulo(5, 5)
print(f"Area: {rectangulo.calcularArea()}")
print(f"Perimetro: {rectangulo.calcularPerimetro()}")