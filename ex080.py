a = (int(input('digite um munero:')), int(input('digite um munero:')),
     int(input('digite um munero:')), int(input('digite um munero:')))
print(f'você digitou os numero {a}')
if 9 in a:
    print(f'o munero 9 apareceu {a.count(9)} vezes')
else:
    print('o munero 9 não apareceu')
if 3 in a:
    print(f'o munero 3 aparece na posição {a.index(3)}')
for n in a:
    if n % 2 == 0:
        print(f'os numero pares são {n}')
