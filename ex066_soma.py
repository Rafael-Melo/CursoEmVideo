print('Digite um valor (Digite 999 para parar!): ')
n = cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma foi {soma}.')
