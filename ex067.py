print('\033[31m-=-'*15)
print(' '*18,'P.A')
print('-=-'*15,'\033[m')
a = int(input('primero termo:'))
a2 = int(input('razão:'))
f = a
t = 1
to = 0
m = 10
while m != 0:
    to = to + m
    while t <= to:
        print('{} > '.format(f), end='')
        f += a
        t += 1
    print('pausa....')
    m=int(input('quantos mais vc quer ?'))
print('foram o total de {} termos'.format(to))
