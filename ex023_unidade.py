num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
if num <= 9999:
    print(f'Milhar: {m}')
    print(f'Centena: {c}')
    print(f'Dezena: {d}')
    print(f'Unidade: {u}')
else:
    print(f'Número {n} inválido!')
