altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é {imc} e você está abaixo do peso.')
elif imc <= 25:
    print(f'Seu IMC é {imc} e você está no peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é {imc} e você está acima do peso.')
elif imc <= 40:
    print(f'Seu IMC é {imc} e você está com obesidade.')    
else:
    print(f'Seu IMC é {imc} e você está com obesidade morbida.')
