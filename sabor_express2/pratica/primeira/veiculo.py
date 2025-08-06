class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._protegido = False
    
    def __str__ (self):
        return f'{self.marca} | {self.modelo} | {self._protegido}'