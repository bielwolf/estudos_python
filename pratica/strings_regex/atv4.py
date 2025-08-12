URL = input('Digite a URL para a validação: ')

if URL.startswith('https://') and URL.endswith('.com'):
    print('A URL está válida.')
else:
    print('A URL não está válida.')
