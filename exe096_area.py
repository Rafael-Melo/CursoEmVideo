def area(l, c):
    area = l * c
    print(f'A área do seu terreno de {l}x{c} é de {area}m².')


# Programa Principal
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
