km = float(input('Digite a distância percorrida (em km): '))

if km == 100:
    valor = km * 10
    print('Valor do pedágio: R$ {:.2f}'.format(valor))
elif 100 < km <= 200:
    valor = km * 20
    print('Valor do pedágio: R$ {:.2f}'.format(valor))
else: 
    valor = km * 30
    print('Valor do pedágio: R$ {:.2f}'.format(valor))  
