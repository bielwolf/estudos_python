despesa = float(input("Digite o total de despesas do mês (R$): "))

salario = 3000.0

if despesa <= salario:
    print("Você tem dinheiro suficiente para pagar suas despesas.")
else:
    print("Atenção! Você ultrapssou o limite do orçamento.")