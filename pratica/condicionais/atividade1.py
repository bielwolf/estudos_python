qtdeM = int(input("Digite a quantidade de maçãs vendidas: "))
qtdeB = int(input("Digite a quantidade de bananas vendidas: "))

if qtdeM > qtdeB:
    print("As maçãs tiveram mais vendas")
elif qtdeM < qtdeB:
    print("As bananas tiveram mais vendas")
else:
    print("As maçãs e bananas tiveram a mesma quantidade de vendas")
