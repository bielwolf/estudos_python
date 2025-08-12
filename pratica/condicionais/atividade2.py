diaA = int(input("Informe os dias para a atividade A: "))
diaB = int(input("Informe os dias para a atividade B: "))
diaC = int(input("Informe os dias para a atividade C: "))

soma = diaA + diaB + diaC

if (diaA >= 0 and diaB >= 0 and diaC >= 0):
    print(f"O tempo total para as atividades é de {soma} dias.")
else:
    print("Erro: os dias não podem ser negativas")  