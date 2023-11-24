a=int(input('digite um numero:'))
c= 0
for b in range(1,a+1):
    if a % b == 0:
        c += 1
        print('\033[32m',end='')
    else:
        print('\033[31m',end='')
    print(b,end=' ')
print('\033[m\nseu numero e {} e dividido {}'.format(a,c))
if c == 2:
    print(' seu numero e primo!')
else:
    print('seu numero não e primo!')
