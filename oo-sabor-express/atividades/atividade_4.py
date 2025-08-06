class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__ (self):
        return f'Conta de {self.titular} - Saldo: {self.saldo} '
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
pessoa1 = ContaBancaria('Maria', 1000)
pessoa2 = ContaBancaria('João', 500)

print(pessoa1)
print(pessoa2)  

pessoa3 = ContaBancaria('Pedro', 2000)
ContaBancaria.ativar_conta(pessoa3)
print(f"{pessoa3._ativo}")
    