x = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        x += c
        count += 1
print(f'A soma de todos os {count} valores solicitados é {x}.')
