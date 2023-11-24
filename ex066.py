print('\033[31m-=-'*15)
print(' '*18,'P.A')
print('-=-'*15,'\033[m')
a = int(input('primeiro termo:'))
a2 = int(input('razão:'))
c = a
t = 1
while t <= 10:
    print(c,'>', end=' ')
    c += a
    t += 1
print('acabou!')
