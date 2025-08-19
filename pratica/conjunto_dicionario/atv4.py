permprincipais = {'leitura', 'escrita', 'execução', 'compartilhamento'}

permsolicitada = set(input('Permissões solicitadas: ').strip().lower().split(', '))

ehsubconjunto = permsolicitada.issubset(permprincipais)

if ehsubconjunto:
    print('As permissões solicitadas fazem parte das permissões principais. ')
else:
    print('As permissões solicitadas não fazem parte das permissões principais. ')
