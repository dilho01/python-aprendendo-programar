l = list()
l2 = list()
print('=-'*30)
while True:
    a = str(input('Nome:'))
    a2 = float(input('Nota 1:'))
    a3 = float(input('Nota 2:'))
    c = (a2 + a3) / 2
    l.append([a, [a2, a3], c])
    a4 = ' '
    while a4 not in 'S/N':
        a4 = str(input('Quer continuar:[S/N]')).strip().upper()[0]
    print('=-'*30)
    if a4 == 'N':
        break
print(f'{"Nu":<4} {"Nome":<4} {"media":<8}')
for i, e in enumerate(l):
    print(f'{i:<4} {e[0]:<4} {e[2]:<8}')
while True:
    print('=-'*30)
    o = int(input('Quer mostre qual media:'))
    if o <= len(l) - 1:
        print(f'A nota do {l[o][0]} são {l[o][1]}')
    o2 = ' '
    while o2 not in 'S/N':
        o2 = str(input('quer continuar:[S/N]')).strip().upper()[0]
    if o2 == 'N':
        break
print(f'{"FIM":-^30}')

