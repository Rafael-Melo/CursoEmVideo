f1 = str(input('Digite uma frase: ')).strip().upper()
print(f1)
f2 = ''.join(f1.split())
print(f2)
# f3 = f2[::-1]
# print(f3)
# if f2 == f3:
#     print('Essa frase é um palíndromo.')
# else:
#     print('Essa frase não é um palíndromo.')
nova = ''
for letra in range(len(f2) -1, -1, -1):
    nova += f2[letra]
if f2 == nova:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')
