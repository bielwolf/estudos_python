import re

cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

padrão = r'(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$'

if padrão.match(cpf):
    print("CPF válido")
else:
    print("CPF inválido") 