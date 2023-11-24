from random import randint
from time import sleep
l = list()
l2 = list()
t2 = 1
print('=-'*20)
print(f'{"MEGA SENA":^33}')
print('=-'*20)
a = int(input('quantos jogos você quer?'))
while t2 <= a:
    t = 0
    while True:
        s = randint(1, 60)
        if s not in l:
            l.append(s)
            t += 1
        if t >= 6:
            break
    l.sort()
    l2.append(l[:])
    l.clear()
    t2 += 1
print(f'{"os muneros sortiandos foram":-^40}')
for c, i in enumerate(l2):
    print(f'jogo {c+1}º:{i}')
    sleep(1)
print(f'{"boa sorte":-^40}')
