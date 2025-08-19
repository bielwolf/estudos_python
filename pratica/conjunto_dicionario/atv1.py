convidados = set()

while True:
    nome = input('Digite o nome do convidado: ')
    if nome == 'sair':
        break
    
    convidados.add(nome)

print(f"Convidados confirmados: {', '.join(convidados)}")
