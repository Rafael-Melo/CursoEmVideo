unidade = input('Digite C para informar um valor em celsius e F para informar um valor em fahrenheit:')
if unidade.lower() == 'c':
    c = float(input('Digite a temperatura em graus celsius:'))
    f = (c * 1.8) + 32
    print(f'A temperatura de {c} graus celsius corresponde a {f} graus fahrenheit')
elif unidade.lower() == 'f':
    f = float(input('Digite a temperatura em graus fahrenheit:'))
    c = (f - 32) / 1.8
    print(f'A temperatura de {f} graus fahrenheit corresponde a {c} graus celsius')
else:
    print('Opção inválida!')
