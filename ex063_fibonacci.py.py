A = 0
B = 1
cont = 3
i = int(input('Quantos termos você quer mostrar? '))
print(f'Sequência de Fibonacci com {i} valores:')
print('Termo 1:')
print(A)
print('Termo 2:')
print(B)
while i >= cont:
    C = A + B
    A = B
    B = C
    if cont > 8000:
        print('É mais de 8000!!!')
    else:
        print(f'Termo {cont}:')
    print(C)
    cont += 1
print('FIM!')
