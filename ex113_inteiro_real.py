def leiaInt(valor):
    while True:
        try:
            numero = int(input(valor))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!! Digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mO usuário não digitou um valor!\033[m')
            return 0
        else:
            return numero


def leiaFloat(valor):
    while True:
        try:
            numero = float(input(valor))
        except (ValueError, TypeError):
            print('\033[1;31mERRO!! Digite um número real valido!\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário não digitou um valor!\033[m')
            numero = 0
            break
        else:
            break
    return numero


# Programa Principal
i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {i} e o número real {r}.')
