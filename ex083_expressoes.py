expressao = str(input('Digite uma expressão: ')).strip()
pilha = []
for v in expressao:
    if v == '(':
        pilha.append('(')
    elif v == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) ==0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
