def somar(n1, n2):
    return n1 + n2

def multiplicar(n1, n2):
    return n1 * n2

def subtrair(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    return n1 / n2

while True:
    try:
        n1 = int(input('Digite um numero: '))
        op = input('Digite uma operação aritimetica: ')
        n2 = int(input('Digite outro numero: '))
    except ValueError:
        print("ERRO: Digite apenas números inteiros!")
        continue

    if op == '+':
        print(f'A soma de {n1} e {n2} é igual a {somar(n1,n2)}')
    elif op == '-':
        print(f'A subtração de {n1} e {n2} é igual a {subtrair(n1, n2)}')
    elif op == '*':
        print(f'A multiplicação de {n1} e {n2} é igual a {multiplicar(n1, n2)}')
    elif op == '/':
        if n2 == 0:
            print('Não existe divisão por 0')
        else:
            print(f'A divisão de {n1} e {n2} é igual a {dividir(n1, n2)}')
    else:
        print('Reveja as informações!')

    sair = input('Se desejar sair aperte "s", caso queira continuar aperte apenas enter: ')
    if sair.lower() == 's':
        print('Obrigado por utilizar')
        break