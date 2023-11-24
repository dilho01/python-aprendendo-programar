s=0
c2=0
for c in range(1,7):
    a=int(input('digite o {} valor:'.format(c)))
    if a %2==0:
        s+=a
        c2+=1
print('vc informou {} numeros pares e a soma foi {}'.format(c2,s))