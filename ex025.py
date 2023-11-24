a=int(input('informe seu numero:'))
n=str(a)
n2=a//10 % 10
n3=a//100 % 10
n4=a//1000 % 10
print(' anlisando o numero {:.2f}...'.format(a))
print('unidade:{}\ndezana:{}\ncentena:{}\nmil1har:{}'.format(n[0],n2,n3,n4))