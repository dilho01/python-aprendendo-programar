from time import sleep
print('--------viagens--------')
a=float(input('quantos km e sua viagem?'))
c=a*0.50
c2=a*0.45
print('CALCULANDO....')
sleep(3)
if c<=200:
    print('sua passagem vai custa {}$,pois tem a distancia {}km'.format(c,a))
else:
    print('sua passaquem vai custa {}$, pois tem a distancia {}km'.format(c2,a))
print('boa viagem!')