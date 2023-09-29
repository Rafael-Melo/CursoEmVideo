print('Digite 999 para parar!')
n = cont = soma = 0
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print(f'Você digitou {cont} números e a soma foi {soma}.')
