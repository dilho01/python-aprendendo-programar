l = []
for c in range(0, 5):
    l.append(int(input(f'digite um valor na posição {c+1}ª:')))
print('=-'*30)
print(f'você digitou os valores {l}')
print(f'o maior valor foi {max(l)} apareceu na posição', end=' ')
for i, v in enumerate(l):
    if v == max(l):
        print(f'{i+1}', end='..')
print(f'\no meenor valor foi {min(l)} e apareceu na posição', end=' ')
for i, v in enumerate(l):
    if v == min(l):
        print(f'{i+1}', end='..')
