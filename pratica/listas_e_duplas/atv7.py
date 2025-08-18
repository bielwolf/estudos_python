resultados = ['Ana', 'Carlos', 'Maria']
print(f'Lista original: {resultados}')

erro = input('Digite o nome incorreto: ')
if erro in resultados:
    correto = input('Digite o nome correto: ')
    posicao = resultados.index(erro)
    resultados.remove(erro)
    resultados.insert(posicao, correto) 
    print(f'O nome {erro} foi substituido por {correto} na lista.')
    print(f'Lista atualizado: {resultados}')
else: 
    print('Nome não encontrado')