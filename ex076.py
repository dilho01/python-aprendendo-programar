print('='*28)
print('{:^28}'.format('BANCO CEV'))
print('='*28)
a = int(input('valor:'))
a2 = a
c = 50
t = 0
while True:
    if a2 >= c:
        a2 -= c
        t += 1
    else:
        if t > 0:
            print(f'o tatol de {t} celula de {c}R$')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        t = 0
        if a2 == 0:
            break
print('-'*28)
print('obrigado pela preferncia\nvolte sempre')