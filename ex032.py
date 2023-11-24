from random import randint
from time import sleep
c=randint(0,5)
print("-=--"*20)
print('vou pensa em um numero entre 0 e 5. tente adivinha ...')
print('-=--'*20)
a=int(input('em qual numero eu pensei ?'))
print('procesando...')
sleep(3)
print('vc acertou {}'if a==c else'vc errou, era {}'.format(c,c))