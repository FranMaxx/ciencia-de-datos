def esPalindromo(cadena):
    texto = cadena.lower()
    return texto == texto[::-1]

palabra = "neuquen"
print(esPalindromo(palabra))