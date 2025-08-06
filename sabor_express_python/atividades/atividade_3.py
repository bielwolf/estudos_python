numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_impares = 0
soma_media = 0
soma = 0
media = 0

nomes = ['João', 'Maria', 'Cleiton', 'Zenitsu']

ano = [2004, 2025]

for nome in nomes: 
    print(f'.{nome}')

print()

for i in numeros:
    if (i % 2 == 1) :
        soma_impares += i
print(f'{soma_impares}')

print()

for i in reversed(numeros):
    if( i <= 10 ):
        print(f'{i}')

print()

numero = int (input('Digite um número: '))
for n in numeros: 
    resultado = numero * n
    print(f'{numero} x {n} = {resultado}')

print()

try: 
    for u in numeros:
        soma += u
    print(f'A soma dos valores é: {soma}')
except:
    print('Erro ao calcular a soma')

try: 
    for l in numeros:
        soma_media += l
        media = soma_media / len(numeros)
    print('A média dos valores é:', media)
except ZeroDivisionError:
    print('Erro ao calcular a média')
except Exception as e: 
    print(f'Ocorreu um erro: {e}')