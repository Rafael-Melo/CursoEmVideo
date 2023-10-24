valores = [[], []]
num = 0
for i in range(1,8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Valores pares: {valores[0]}')
print(f'Valores ímpares: {valores[1]}')
