def conversaoparaint(lista):
    return [int(telefone) for telefone in lista]

def verificar_tipos(lista):
    for num in lista:
        if not isinstance(num, int):
            return "Erro na conversão"
        return "Todos os números foram convetidos corretamente!"


telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
numerosint = conversaoparaint(telefones)
print(verificar_tipos(numerosint))