l = []
c = c2 = 0
while True:
    a = int(input('digite um valor:'))
    c += 1
    l.append(a)
    a2 = ' '
    while a2 not in 'NS':
        a2 = str(input('quer continur?[S/N]')).strip().upper()[0]
    if a2 == 'N':
        break
l.sort(reverse=True)
print(f'você digitou {c} elementos')
print(f'os numeros em ordem degrecente são: {l}')
if a == 5:
    c2 += 1
    print(f'o numero 5 apareceu {c2} vezes')
else:
    print('o numero 5 não apareceu')
