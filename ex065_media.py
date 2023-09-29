continuar = 'S'
soma = maior = menor = cont = 0
while continuar in 'S':
        n = int(input('Digite um número: '))
        soma += n
        cont += 1
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n  
        continuar = str(input('Quer digitar mais números? (S/N) ')).strip().upper()[0]
media = soma / cont
print(f'Você digitou {cont} valores.\nA média entre esses valores é {media}.\nO maior valor foi {maior} e o menor valor foi {menor}.')
print('Fim')
