n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f'Ordem dos números do maior para o menor é {n1}, {n2} e {n3}.')
        else:
            print(f'Ordem dos números do maior para o menor é {n1}, {n3} e {n2}.')
    else:
        print(f'Ordem dos números do maior para o menor é {n3}, {n1} e {n2}.')
elif n2 > n1:
    if n2 > n3:
        if n1 > n3:
            print(f'Ordem dos números do maior para o menor é {n2}, {n1} e {n3}.')
        else:
            print(f'Ordem dos números do maior para o menor é {n2}, {n3} e {n1}.')
    else:
        print(f'Ordem dos números do maior para o menor é {n3}, {n2} e {n1}.')
else:
    print('Números repetidos')
