matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
par = tercoluna = seglinha = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            tercoluna += matriz[l][c]
        if l == 1 and c == 0:
            seglinha = matriz[l][c]
        else:
            if l == 1 and seglinha < matriz[l][c]:
                seglinha = matriz[l][c]
print('*-' * 30)            
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('*-' * 30)
print(f'A soma dos valores pares da matriz é {par}')
print(f'A soma dos valores da terceira coluna é {tercoluna}')
print(f'O amior valor da segunda linha é {seglinha}')
