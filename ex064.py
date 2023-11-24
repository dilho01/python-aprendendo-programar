n=float(input('digite um numero:'))
n2=float(input('digitee um numero:'))
ma=0
c=0
while c  != 5:
    c = int(input('[1] soma\n[2] multiplicar\n[3] maior\n[4] novo numero\n[5] sair do programa\nqual e sua opição:'))
    if c == 1:
        s=n+n2
        print('a soma entre {},{} e {}'.format(n,n2,s))
    elif c == 2:
        m=n*n2
        print('a multilpição entre {},{} e {}'.format(n,n2,m))
    elif c == 3:
        ma = n
        ma = n2
        if n > n2:
            n2 = n
        elif n2 > n:
            n = n2
        print('0 maior e {}'.format(ma))
    elif c == 4:
        print('Informe os numeros nova mente')
        n=float(input('digite um numero:'))
        n2=float(input('digite um numero:'))
    elif c == 5:
        print('acabou!')
    else:
        print('opição invaliida')
