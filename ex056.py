print('='*21,'\n10 termos de um P.A\n','='*21)
a=int(input('primero termo:'))
a2=int(input('razão:'))
s=a+(10-1)*a2
for c in range(a,s+a2,a2):
    print('{},'.format(c),end=' ')
print('acabou!')