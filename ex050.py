from random import randint
from time import sleep
print('\033[32m#'*30)
print('         vamos jogar')
print('#'*30,'\033[m')
print('''ESCOLHA SUA OPIÇÃO
[1]pedra
[2]papel
[3]tesoura''')
a=int(input('qual vc escolhe? '))
print('\033[33mJO\033[m')
sleep(1)
print('\033[34mKEN\033[m')
sleep(0.8)
print('\033[32mPO!\033[m')
i=('pedra', 'papel', 'tesoura')
c=randint(1, 3)
print('------o conputador escolheu------\n     ========={}========='.format(i[c]))
if c==1:
    if a==1:
        print('\033[33mEMPATE\033[!')
    elif a==2:
        print('\033[32mVC GANHOU!\033[m')
    elif a==3:
       print('\033[31mVC PERDEU!\033[m')
    else:
        print('ESSA OPIÇÃO NÃO EXISTE!')
elif c==2:
    if a==1:
        print('\033[31mVC PERDEU!\033[m')
    elif a==2:
        print('\033[33mEMPATE!\033[m')
    elif a==3:
        print('\033[32m VC GANHOU!\033[m')
    else:
        print('ESSA OPIÇÃO NÃO EXISTE!')
elif c==3:
    if a==1:
        print('\033[32mVC GANHOU!\033[m')
    elif a==2:
        print('\033[31mVC PERDEU!\033[m')
    elif a==3:
        print('\033[33mEMPATE!\033[m')
    else:
        print('ESSA OPIÇÃO NÃO EXISTE!')