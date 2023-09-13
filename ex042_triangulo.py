r1 = float(input('Digite o tamanho da primeira reta em centímetros: '))
r2 = float(input('Digite o tamanho da segunda reta em centímetros: '))
r3 = float(input('Digite o tamanho da terceira reta em centímetros: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 and r1 == r3:
        print('Essas retas podem formar um triangulo \033[1;32mEquilátero\033[m.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Essas retas podem formar um triangulo \033[1;32mIsósceles\033[m.')
    else:
        print('Essas retas podem formar um triangulo \033[1;32mEscaleno\033[m.')
else:
    print('Essas retas não podem formar um triangulo')
