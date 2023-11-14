def leiaInt(valor):
    while True:
        numero = input(valor)
        if numero.isnumeric() == True:           
            break
        else:
            print('\033[1;31mERRO!! Digite um número inteiro válido!\033[m')
    return numero


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
