l = list()
l2 = list()
while True:
    a = str(input('nome:'))
    a2 = int(input('peso:'))
    l.append(a)
    l.append(a2)
    l2.append(l[:])
    l.clear()
    a3 = ' '
    while a3 not in 'SN':
        a3 = str(input('quer continuar?[S/N]')).strip().upper()[0]
    if a3 == 'N':
        break
print('=-'*30)
print(f'ao todo, você cadastrou {len(l2)}')
print(f'o maior peso foi {max(l2)}Kg.')
print(f'o menor peso foi {min(l2)}Kg.')
print('=-'*30)
