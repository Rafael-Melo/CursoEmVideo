valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('-' * 30)
print(f'Você digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'Lista em ordem decrescente: {valores}')
if 5 in valores:
    print(f' O valor 5 foi digitado na posição {valores.index(5)}')
else:
    print('O valor 5 não foi encontrado n lista')

