voluntarios = []

while True:
    nome = input("Digite o nome do voluntário(ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    voluntarios.append(nome)

print(f'Voluntários registrados: {voluntarios}')