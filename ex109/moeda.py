def aumentar(valor = 0, aumento = 0, formato = False):
    res = valor + (valor * (aumento / 100))
    return res if formato is False else moeda(res)
    

def diminuir(valor = 0, reducao = 0, formato = False):
    res = valor - (valor * (reducao / 100))
    return res if formato is False else moeda(res)

def dobro(valor = 0, formato = False):
    res = valor * 2
    return res if formato is False else moeda(res)

def metade(valor = 0, formato = False):
    res = valor / 2
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.',',')

