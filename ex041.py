c=float(input('qual e valor da casa?'))
g=float(input('quanto vc ganha?'))
q=float(input('quantos anos vc vai pagar a casa?'))
c1=c/(q*12)
c2=g*30/100
if c1<c2:
    print('seu parcelamento foi aceito, as parcelas sao {:.2f}'.format(c2))
else:
    print('seu parcelamento nao foi aceito, pois e mais que 30% do seu salario')