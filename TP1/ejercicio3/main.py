import math

def calcularArea(radio):
    return math.pi * (radio ** 2)

radio = 3
area = calcularArea(radio)
print(f"El area es: {area}")