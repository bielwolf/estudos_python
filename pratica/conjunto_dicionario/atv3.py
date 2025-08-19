laura = set(input('Lista da laura: ').split(', '))
ana = set(input('Lista da ana: ').split(', '))

comum = laura.intersection(ana)
print(f"Itens em ambas as listas: {', '.join(comum)}")

exlaura = laura.difference(ana)
print(f"Itens exclusivos de Laura: {', '.join(exlaura)}")

exdaana = ana.difference(laura)
print(f"Itens exclusivos de Ana: {', '.join(exdaana)}")
