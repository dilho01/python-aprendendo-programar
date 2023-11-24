from random import randint
v = 0
print('-='*20)
print('       vamos jogar Impar ou Par')
print('-='*20)
while True:
    n = int(input('digite um valor:'))
    c = randint(0, 10)
    s = c + n
    n2 = ' '
    while n2 not in 'PI':
        n2 = str(input('PAR ou IMPAR?[P/I]')).strip().upper()[0]
    print(f'vc jogou {n} e o computador jogou {c}.O total foi {s}', end=' ')
    print('deu PAR'if s % 2 == 0 else 'deu IMPAR')
    if n2 == 'P':
        if s % 2 == 0:
            print('VC VENCEU!')
            v += 1
        else:
            print('VC PERDEU!')
            break
    elif n2 == 'I':
        if s % 2 != 0:
            print('VC GANHOU!')
            v += 1
        else:
            print('VC PERDEU!')
            break
    print('vamos jogar novamente....')
print(f' vc perdeu e ganho {v}')
