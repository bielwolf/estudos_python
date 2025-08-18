lista = ["Arroz", "Feijão", "Carne", "Frango", "Ovo"]

item = input("Digite o item que você verificar: ")
if item in lista:
    print(f"O item {item} está na lista.")
else:
    print(f"O item {item} precisa ser comprado.")
print(lista)