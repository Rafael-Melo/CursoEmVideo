from time import sleep
def maior(*num):
    maior = cont = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    for n in num:
        if cont == 0 or n > maior:
            maior = n
            cont += 1
        print(f'{n}', end=' ')
        sleep(0.5)
    print('')
    print(f'Foram informados {cont} valores ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {maior}.')
    sleep(1)
    print('-=' * 30)
    sleep(1)


# Programa Principal
maior(1, 2, 30, 6, 17, 8, 9)
maior(19, 2, 13, 6, 17)
maior(10, 2, 30, 6, 71, 8, 29, 35)
maior(8)
maior()
