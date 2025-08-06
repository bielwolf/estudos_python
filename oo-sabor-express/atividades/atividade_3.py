class Pessoa:
    pessoas = []

    def __init__(self, nome, profissao, idade=0):
        self.nome = nome.title()
        self._profissao = profissao.title()
        self.idade = idade
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self.nome}, {self._profissao}, {self.idade}'

    def aniversario(self):
        self.idade += 1

    @classmethod
    def mostrar_pessoas(cls):
        print(f"{'Nome da pessoa'.ljust(25)} | {'Profissão'.ljust(25)} | {'Idade'}")
        for pessoa in cls.pessoas:
            print(f"{pessoa.nome.ljust(25)} | {pessoa._profissao.ljust(25)} | {str(pessoa.idade)}")

    @property
    def saudacao(self):
        return f'Olá, {self.nome}, Bem vindo ao seu trabalho de {self._profissao}!'

    
pessoa1 = Pessoa('Gabriel', 'Programador', 25)
pessoa1.mostrar_pessoas()