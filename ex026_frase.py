frase = str(input('Digite uma frase: ')).strip()
print(f'A letra "a" aparece {frase.lower().count("a")} vezes.')
print(f'A letra "a" aparece pela primeria vez na posição {frase.lower().find("a")}.')
print(f'A letra "a" aparece pela última vez na posição {frase.lower().rfind("a")}.')
