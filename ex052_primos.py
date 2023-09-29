from math import sqrt, ceil
n = int(input('Digite um número: '))
primo = 0
if n > 1:
    r = sqrt(n)
    for c in range(2, ceil(r)+1):
        if n % c == 0:
            primo += 1
    if primo > 0:
        print('Esse número não é primo.')
    else:
        print('Esse número é primo.')      
else:
    print('Esse número não é primo.')
