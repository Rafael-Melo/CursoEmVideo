def fatorial(n, show=False):
    """
    -=> Calcula o fatorialde um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


# Programa Principal
print(fatorial(5, show=True))
help(fatorial)
