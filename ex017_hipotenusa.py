from math import hypot
cata = float(input('Digite o valor do cateto adjacente: '))
cato = float(input('Digite o valor do cateto oposto: '))
hip = hypot(cata, cato)
print(f'O valor da hipotenusa é {hip:.2f}')
