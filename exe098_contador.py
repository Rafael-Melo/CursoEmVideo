from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i > f:
        for c in range(i, f-1, p * -1):
            sleep(0.5)
            print(f'{c}', end=' ')
        print('FIM!')
        sleep(1)
    else:
        for c in range(i, f+1, p):
            sleep(0.5)
            print(f'{c}', end=' ')
        print('FIM!')
        sleep(1)


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
