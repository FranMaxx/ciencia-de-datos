class Rectangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def calcularArea(self):
        return self.alto * self.ancho

    def calcularPerimetro(self):
        return 2 * (self.alto + self.ancho)

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

cuadrado = Cuadrado(5)
print(f"Area: {cuadrado.calcularArea()}")
print(f"Perimetro: {cuadrado.calcularPerimetro()}")