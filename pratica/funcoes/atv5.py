def convETotal(valores):
    inteiros = [int(valor) for valor in valores]
    return sum(inteiros)

valores = input("Digite os valores das vendas: ").split()
print(f'O toal de vendas foi: {convETotal(valores)}')