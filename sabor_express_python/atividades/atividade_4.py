pessoa = {'nome': 'Gabriel', 'idade': 20, 'cidade': 'Fortaleza'}
pessoa2 = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}

pessoa['idade'] = 21
pessoa['profissao'] = 'Programador'
del pessoa ['cidade']
print(pessoa)
print()


numeros_relacionados = {1, 2, 3, 4, 5}
for i in numeros_relacionados:
    quadrados = i ** 2
    print(f'O quadrado de {i} é {quadrados}')
    print()

if 'nome' in pessoa2:
    print('O dicionário contém a chave "nome"')
else:
    print('O dicionário não contém a chave "nome"')
