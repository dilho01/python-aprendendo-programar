from random import randint
print('''eu sou seu  computador...
acabei de oensar em um numero entre 0 e 10
sera que você consegue adivilhar qual e ?''')
p=randint(0,11)
c=int(input('qual numero eu pensei ?'))
while p != c:
    if p > c:
        print('MAIS... tente mais um vez')
    elif p < c:
        print('MENOS... tente mais um vez')
    c=int(input('quaal e suaa escolha:'))
print('o numero e era {} você acertou!'.format(p))
