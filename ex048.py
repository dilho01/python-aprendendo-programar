k=float(input('quantos kg vc pesa?'))
a=float(input('qual e sua altura:'))
c=k/a**2
if c<18.5:
    print('abaixo do peso')
elif c>18.5 and c<25:
    print('peso ideal')
elif c>25 and c<30:
    print('sobre peso')
elif c>30 and c<40:
    print('obesidade')
elif c>40:
    print('obesidade morbida')
