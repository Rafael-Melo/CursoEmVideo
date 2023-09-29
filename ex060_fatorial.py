from time import sleep
n = int(input('Digite um número para calcular seu fatorial: '))
cont = n
res = n
print(f'{n}!',end=" = ")
sleep(0.5)
print(f'{n}',end=" ")
sleep(0.5)
while cont > 1:
    cont -= 1
    res = res * cont
    print(f'x {cont}',end=" ")
    sleep(0.5)
print(f'= {res}')
