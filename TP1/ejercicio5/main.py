def calcularPariedad(a):
    return "par" if a % 2 == 0 else "impar"

n = 10
print(f"El número {n} es {calcularPariedad(n)}")