from random import randint
a = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os numeros sortiados foram:', end=' ')
for n in a:
    print(f',{n}',end=' ')
print(f'\no mairo munero foi {max(a)}')
print(f'o menor numero foi {min(a)}')
