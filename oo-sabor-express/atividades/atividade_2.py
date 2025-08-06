class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro_especifico = Carro('Ferrari', 'Vermelho', 2020)

class Restaurante:
    def __init__(self, nome, categoria, ativo, endereco, telefone):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.endereco = endereco
        self.telefone = telefone
    
    def __str__(self):
        return f'{self.nome} - {self.categoria}'
    
restaurante_italiano = Restaurante('Bella Vita', 'Italiano', False, 'Rua 1', '12345678')
print(restaurante_italiano)

class Cliente:
    def __init__(self, nome, idade, telefone, endereco):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco

cliente_vip = Cliente( 'João', 30, '12345678', 'Rua 1')
cliente_2 = Cliente('Maria', 25, '98765432', 'Rua 2')
cliente_3 = Cliente ('Pedro', 40, '11111111', 'Rua 3')