a = input('Digite algo:')
print(f'O tipo primitivo de {a} é', type(a))
print(f'{a} só tem espaços?', a.isspace())
print(f'{a} é um número?', a.isnumeric())
print(f'{a} é alfabetico?', a.isalpha())
print(f'{a} é alfanumerico?', a.isalnum())
print(f'{a} está em maiúsculas?', a.isupper())
print(f'{a} está em minúsculas?', a.islower())
print(f'{a} está captalizada?', a.istitle())

