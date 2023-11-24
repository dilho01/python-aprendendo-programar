n = int(input('digite um numero [999 PARA PARAR]:'))
c = t = 0
while n != 999:
    c += 1
    t += n
    n = int(input('digite um numero [999 PARA PARAR]:'))
print('você digitou {} numero e a somo entre eles são {}'.format(c,t))
