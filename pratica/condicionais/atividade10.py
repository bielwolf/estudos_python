renda = float(input('Digite o valor da sua renda mensal: '))
parcela = float(input('Digite o valor da parcela: '))

calculo = renda * 0.3

if renda > 2000 and parcela < calculo:   
    print('Empréstimo aprovado!')
elif renda <= 2000:
    print('Empréstimo negado: renda insuficiente.')
else:
    print('Empréstimo negado: parcela abaixo de 30 porcento da renda.')