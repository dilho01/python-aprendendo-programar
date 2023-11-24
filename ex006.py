n1=int(input('digite um numore:'))
n2=int(input('digite mais um numero:'))
s=n1+n2
sb=n1-n2
m=n1*n2
d=n1/n2
di=n1//n2
so=n1**n2
print('a soma e {} a sobritaçao e {} a mutiplicaçao {}'.format(s,sb,m),end='')
print('divicçao e {:.3f} e a diviçao intera e {} sobre {}'.format(d,di,so))