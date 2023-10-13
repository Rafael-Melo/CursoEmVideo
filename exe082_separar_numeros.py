valores = []
par = []
impar = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-' * 30)
print(f'A lista que você digitou foi: {valores}')
print(f'Essa é uma lista somente com o números pares: {par}')
print(f'Essa é uma lista somente com o números ímpares: {impar}')
