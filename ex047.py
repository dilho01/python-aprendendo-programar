r1=float(input('primeira reta:'))
r2=float(input('segunda reta:'))
r3=float(input('terceira reta:'))
if r1<r2+r3 and r2<r1+r3 or r3<r1+r2:
    print('as retas acima podem formão um triangulo' , end=' ')
    if r1==r2==r3:
        print('equilatero!')
    elif r1 != r2 != r3 != r1:
        print('escaleno!')
    else:
        print('isosceles!')
else:
    print('as retas não formão um triangulo')