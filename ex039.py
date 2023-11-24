print(10*'=','como formar um triangulo','='*10)
r1=float(input('digite um reta:'))
r2=float(input('digite um reta:'))
r3=float(input('digite um reta:'))
if r1 < r2+r3 and r2 < r1+r3 or r3 < r1+r2 :
    print(' esse meditas formal um triangulo')
else:
    print('esse meditas nao fornal um triangulo')