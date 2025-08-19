participantes = { 
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
} 

nome_removido = input("Nome do participante a ser removido: ")

for workshop, nomes in participantes.items():
    nomes.discard(nome_removido)
print('Lista atualizada de participantes: ')

for worshop, nomes in participantes.items():
    print(f'{workshop}: {nomes}')