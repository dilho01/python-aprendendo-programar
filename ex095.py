a = dict()
a['nome'] = str(input('Nome:'))
a['media'] = float(input(f'Media do {a["nome"]}:'))
if a['media'] >= 7:
    a['situação'] = 'aprovado'
elif 5 >= a['media'] < 7:
    a['situação'] = 'recuperação'
else:
    a['situação'] = 'reprovado'
print('=-'*30)
for k, e in a.items():
    print(f'*{k} =',end=' ')
    print(f'{e}')
