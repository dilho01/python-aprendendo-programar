c=int(input(' digite um numero para calcular o fatorial:'))
s=c
f=1
print('calculando o fatorial {}!...'.format(c),)
while s > 0:
    print('{}'.format(s), end='')
    print('! x ' if s>1 else ' = ', end= '')
    f*=s
    s-=1
print('{}'.format(f))