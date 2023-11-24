from random import shuffle
a1=str(input('nome:'))
a2=str(input('nome:'))
a3=str(input('nome:'))
a4=str(input('nome:'))
li=[a1,a2,a3,a4]
shuffle(li)
print('a ordem e {}'.format(li))