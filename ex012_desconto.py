vprod = float(input('Digite o valor do produto:'))
porcentagem = float(input('Digite  a porcentagem do desconto:'))
desconto = vprod * porcentagem / 100
print(f'O produto custa R${vprod:.2f} e na promoção com desconto de {porcentagem}% vai custar R${vprod - desconto:.2f}')
