lista = ('zero', 'um', 'dois','três', 'quatro', 'cinco','seis', 'sete', 
      'oito', 'nove','dez', 'onze', 'doze', 'treze','quatorze', 'quinze',
      'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num not in range (0, 21):
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {lista[num]}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('FIM!')
