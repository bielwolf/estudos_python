hora = int(input("Digite a hora atual (formato 24h): "))

if 8 <= hora <= 18:
    print("Acesso liberado!")
else:
    print("Acesso negado!")