def fibonacci(n):
    if n < 1:
        return []
    elif n == 1:
        return [0]

    serie = [0, 1]

    for i in range(2, n):
        siguiente = serie[-1] + serie[-2]
        serie.append(siguiente)

    return serie

n = 20
print(fibonacci(n))