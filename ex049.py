print('='*10,'loja do gabriel','='*10)
a=float(input('digide seu valor:'))
print('[1]dinheiro')
print('[2]á vista no cartao')
print('[3]parcelado em 2x no carãto')
print('[4]parecelado em 3x ou mais no cartão')
a2=int(input('qual e sua opição?'))
c=a*10/100
c2=a*5/100
c3=a*20/100
if a2==3:
    input('quantas vezes?')
    print('nao tem desconto o valor a apagar e de {}$'.format(a))
elif a2==1:
    print('sua compra foi de {}$ e seu desconto e de {}$ o valor apagar e {}$'.format(a,c,a-c))
elif a2==2:
    print('sua compra de {}$ e seu desconto e de {}$ o valor apagar e de {}$'.format(a,c2,a-c2))
elif a2==4:
    input('qunatas vezes?')
    print('sua compra foi {}$ e seu juros e de {}$ o valor apagar e de {}$ '.format(a,c3,c3+a))