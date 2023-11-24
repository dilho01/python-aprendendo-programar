from random import randint
from time import sleep
from operator import itemgetter
a = {'jogador1': randint(1, 6),
     'jogador2': randint(1, 6),
     'jogador3': randint(1, 6),
     'jogador4': randint(1, 6)}
c = c2 = 0
for e in a.values():
    c += 1
    print(f'o jogador{c}º tirou {e} no dado')
    sleep(1)
print('=-'*30)
print(f'{"RANKIGN DOS JOGADORES":=^30}')
a2 = list()
sleep(1)
a2 = sorted(a.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(a2):
    c2 += 1
    print(f'{c2}ºluga: {v[0]} com {v[1]}')
    sleep(1)
