from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('-=-' * 25)
    print("""Escolha uma opção:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA""")
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} e {n2} é {soma}.')
    elif opcao == 2:
        mult = n1 * n2
        print(f'O produto de {n1} e {n2} é {mult}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior do que {n2}.')
        elif n1 < n2:
            print(f'{n1} é menor do que {n2}.')
        else:
            print(f'{n1} é igual {n2}.')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizado!')
    else:
        opcao = int(input('Opção inválida, escolha novamente: '))
    print('-=-' * 25)
    sleep(2)
