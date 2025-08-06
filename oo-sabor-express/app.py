from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 9)
restaurante_praca.receber_avaliacao('João', 8)
restaurante_praca.receber_avaliacao('Maria', 5)

def main():
    Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()