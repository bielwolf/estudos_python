def calculoidade(nascimento, atual):
    return atual - nascimento

nascimento = int(input("Digite seu ano de nascimento: "))
atual = int(input("Digite o ano atual: "))

idade = calculoidade(nascimento, atual)
print(f'A idade é {idade} anos!')