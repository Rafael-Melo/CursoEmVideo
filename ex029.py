vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    vel2 = vel - 80
    multa = vel2 * 7
    print(f'Você estava a {vel}Km/h, {vel2}km/h a cima do limite. Vai receber uma multa de {multa}.')
else:
    print('Tudo limpo!')
