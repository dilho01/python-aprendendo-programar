a=float(input('primero valor?'))
a2=float(input('segundo valor?'))
a3=float(input('terceiro valor?'))
if a2>a and a3>a:
    m=a
if a>a2 and a3>a2:
    m=a2
if a>a3 and a2>a3:
    m=a3
print('o menor valor e {:.2f}'.format(m))
if a2<a and a3<a:
    mi=a
if a<a2 and a3<a2:
    mi=a2
if a3>a and a3>a2:
    mi=a3
print('o maoir numero e {:.2f}'.format(mi))