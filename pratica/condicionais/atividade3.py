temp = float(input("Digite a temperatura atual: "))

if temp > 25:
    print("Alerta! Temperatura acima do limite permitido")
elif temp == 25:
    print("Temperatura dentro do limite permitido")
else:
    print("Temperatura abaixo do limite permitido")