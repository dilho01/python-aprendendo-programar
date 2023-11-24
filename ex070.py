n2 = 'S'
c = ma = s = t = me = 0
while n2 in 'Ss':
    n = int(input('digite um numero:'))
    s += n
    c += 1
    if c == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    n2 = str(input('quer continuar?[S/N]')).strip().upper()[0]
t = s / c
print('você digitou {} numeros e a media foi {:.2f} e o maior numero e {} e o menor numero e {}'.format(c,t,ma,me))
