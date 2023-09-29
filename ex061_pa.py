n = int(input('Digite um número: '))
razao = int(input('Digite uma razão: '))
termo = n
total = 0
mais = 10
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=" - ")
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos.')
