convidados = ['Ana', 'Carlos', 'Daniel']
print(f'Lista atual de convidados: {convidados}')

nome = input('Digite o nome do novo convidado: ')
posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))
convidados.insert(posicao - 1, nome)

print(f'Lista atual de convidados: {convidados}')