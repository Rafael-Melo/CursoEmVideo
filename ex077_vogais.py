palavras = ('Ultima', 'Analise', 'Trabalhar', 'TI', 'Gostar', 'Tecnologia',
         'Desafiador', 'Abordagem', 'Apoio', 'Adequado', 'Python')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
