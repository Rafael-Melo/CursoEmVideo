n = int(input('Digite um número: '))
razao = int(input('Digite uma razão: '))
termo = n
cont = 1
while cont <= 10:
    print(termo, end=" - ")
    termo += razao
    cont += 1
print('FIM')
