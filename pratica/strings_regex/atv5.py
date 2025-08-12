import re

texto = input ("Digite um texto: ")
numero = re.findall(r'\d+', texto)[0]
print(f'O número da receita é: {numero}')