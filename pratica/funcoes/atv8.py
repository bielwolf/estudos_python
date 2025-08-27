soma = lambda num1, num2: num1 + num2
sub = lambda num1, num2: num1 - num2
mult = lambda num1, num2: num1 * num2
div = lambda num1, num2: num1 / num2

def escolha(operacao, num1, num2):
    match operacao:
        case "+":
            return soma(num1, num2)
        case "-":
            return sub(num1, num2)
        case "*":
            return mult(num1, num2)
        case "/":
            return div(num1, num2)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (| + | - | * | / |): ")

calculo = escolha(operacao, num1, num2)
print(f"O resultaso é: {calculo}")