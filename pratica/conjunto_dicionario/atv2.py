texto1 = set(input('Digite seu texto: ').lower().split())
texto2 = set(input('Digite seu texto: ').lower().split())

comuns = texto1.intersection(texto2)

print(comuns)