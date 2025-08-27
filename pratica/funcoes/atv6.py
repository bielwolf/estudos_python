def filtroPar(numeros):
    inteiros = [int(num) for num in numeros]
    pares = list(filter(lambda x:x % 2 == 0, inteiros))
    return pares

numeros = input("Digite os números separados por espaço: ").split()
pares = filtroPar(numeros)
print(f'Números pares: {pares}')