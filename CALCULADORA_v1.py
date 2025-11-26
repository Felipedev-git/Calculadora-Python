while True:
    try:
        n1 = int(input('DIGITE UM NUMERO: '))
        op = input('QUAL SERÁ A OPERAÇÃO ARITIMETICA? ')
        n2 = int(input('DIGITE OUTRO NUMERO: '))
    except ValueError:
        print('Digite um numero real!')
        continue    
    if op == '-':
        print(f'A subtração de {n1} e {n2} é = {n1 - n2}')
    elif op == '+':
        print(f'A adição entre {n1} e {n2} é {n1 + n2}')
    elif op == '/':
        if n2 == 0:
            print('Não posso dividir por 0')
        else:
            print(f'A divisão entre {n1} e {n2} é {n1 / n2}')   
    elif op == '*':
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    else:
        print('Reveja as informações!')
    sair = input('Deseja Sair? Digite "s" ou "enter" para continuar: ')
    if sair.lower() == 's':
        print('Obrigado por ultilizar!')
        break
    