def somaXNumeros(n):
    if n == 0:
        return 0
    return n + somaXNumeros(n-1)

print(somaXNumeros(10))