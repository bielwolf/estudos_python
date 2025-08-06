def teste_para_par_ou_impar():
    print('Teste para par ou impar')
    par_ou_impar = int(input('Insira um número: '))

    if par_ou_impar % 2 == 0:
        print(f'{par_ou_impar} é par')
    else:
        print(f'{par_ou_impar} é impar')
    
    print('Fim do teste\n')

def idade_usuario():
    print('Teste para testar sua idade')
    idade = int(input('Insira sua idade: '))

    if 0 < idade <= 12:
        print('Você é criança')
    elif 13 < idade <= 18:
        print('Você é adolescente')
    else:
        print('Você é adulto')

    print('Fim do teste\n')

def entrada_usuario():
    print('Teste para testar a entrada do usuário')
    nome = input('Insira seu nome: ')
    senha = input('Insira sua senha: ')

    nome_usuario = 'Gabriel'
    senha_usuario = '1234'

    if nome == nome_usuario and senha == senha_usuario:
        print('Bem-vindo!')
    else:
        print('Senha ou nome incorreto')

    print('Fim do teste\n')

def coordernadas():
    print('Teste para testar as coordenadas')
    x = int(input('Insira a coordenada x: '))
    y = int(input('Insira a coordenada y: '))

    if x > 0 and y > 0:
        print('Primeiro quadrante')
    elif x < 0 and y > 0:
        print('Segundo quadrante')
    elif x < 0 and y < 0:
        print('Terceiro quadrante')
    elif x > 0 and y < 0:
        print('Quarto quadrante')
    else: 
        print('Origem')

teste_para_par_ou_impar()
idade_usuario()
entrada_usuario()
coordernadas()    
