class ClienteBanco:
    def __init__(self, nome, saldo): #adionar cpf, idade e profissao quando for utilizar
        self.nome = nome
        # self.cpf = cpf
        # self.idade = idade
        # self.profissao = profissao
        self.saldo = saldo

    @classmethod
    def criar_conta(cls, nome, saldo):
        conta = ClienteBanco(nome, saldo)
        return conta


# cliente1 = ClienteBanco("João", 123456789, 30, "Engenheiro", 1000.00)
# cliente2 = ClienteBanco("Maria", 987654321, 25, "Advogada", 500.00)
# cliente3 = ClienteBanco("Pedro", 111111111, 40, "Médico", 2000.00)

conta = ClienteBanco.criar_conta('Ana', 1500.00)
print(f'A conta de {conta.nome} criada com o saldo de {conta.saldo}')

# print(f'{cliente1}')