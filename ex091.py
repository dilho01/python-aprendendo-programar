a = [[], []]
a2 = 0
for c in range(1, 8):
    a2 = (int(input(f'digite o {c}ª valor:')))
    if a2 % 2 == 0:
        a[0].append(a2)
    else:
        a[1].append(a2)
a[0].sort()
a[1].sort()
print('=-'*30)
print(f'os valores paress são: {a[0]}')
print(f'os valores impares são: {a[1]}')
print('=-'*30)
