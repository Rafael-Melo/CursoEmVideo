print('=' * 30)
print('{:^30}'.format('BANCO DINHEIROS'))
print('=' * 30)
saque = int(input('Qual valor você quer sacar? R$ '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
# cinqueta = vinte = dez = um = 0
# while saque >= 50:
#     saque -= 50
#     cinqueta += 1
# while saque >= 20:
#     saque -= 20
#     vinte += 1
# while saque >= 10:
#     saque -= 10
#     dez += 1
# while saque >= 1:
#     saque -= 1
#     um += 1
# print('TOTAL:')
# if cinqueta >= 0:
#     print(f'{cinqueta} cédulas de R$50')
# if vinte >= 0:
#     print(f'{vinte} cédulas de R$20')
# if dez >= 0:
#     print(f'{dez} cédulas de R$10')
# if um >= 0:
#     print(f'{um} cédulas de R$1')
print('=' * 30)
print('Volte sempre!')
